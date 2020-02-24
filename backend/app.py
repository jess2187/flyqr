from flask import Flask, jsonify, request, redirect, send_file
from flask_api import status
from celery import Celery
import config
from objects import gen_organization, gen_campaign, gen_flyer
from SqlHelper import SqlHelper
from AuthUtils import AuthUtils
from flask_bcrypt import Bcrypt
import response_utils as Resp
from FlyerDAO import get_flyer_dao_from_qr_code
from secrets import token_hex
from pdfqr import PDF_QR

app = Flask(__name__)

app.config['MYSQL_HOST'] = config.host
app.config['MYSQL_USER'] = config.user
app.config['MYSQL_PASSWORD'] = config.passwd
app.config['MYSQL_DB'] = config.db
app.config['CELERY_BROKER_URL'] = config.CELERY_BROKER_URL
app.config['CELERY_RESULT_BACKEND'] = config.CELERY_RESULT_BACKEND

celery = Celery(app.name, broker=app.config["CELERY_BROKER_URL"])
celery.conf.update(app.config)

sql = SqlHelper(app)
bcrypt = Bcrypt(app)
auth = AuthUtils(sql, bcrypt)

# URL_INTO_EXPO_APP = 'exp://exp.host/@evanram/flyqr?code=%s'
URL_INTO_EXPO_APP = 'exp://localhost:19000?code=%s'
ANALYTICS_URL = 'https://881c6e7a.ngrok.io/x/'

@app.route('/ping')
def ping():
    return "pong"

#
# Authentication
#

@app.route('/auth/register', methods = ['POST'])
def register_org():
    req_data = request.values
    name = req_data['name']
    email = req_data['email'].lower()
    password = req_data['password']

    if auth.accountExists(email):
        return Resp.conflictAccountExists()

    auth.createUser(name, email, password)

    return Resp.okNoContent()

@app.route('/auth/login', methods = ['POST'])
def login_org():
    req_data = request.values
    email = req_data['email'].lower()
    password = req_data['password']

    if not auth.checkUser(email, password):
        return Resp.unauthorized()

    token = auth.createTokenForOrgGivenEmail(email)

    return Resp.heresYourToken(token)

@app.route('/auth/logout', methods = ['POST'])
def logout_org(): # does not logout everywhere
    req_data = request.values
    token = req_data['token']

    org_id = auth.getOrgIdFromToken(token)

    if org_id is None:
        return Resp.unauthorized()

    auth.deleteToken(token)

    return Resp.okNoContent()

#
# Analytics
#

@app.route('/x/<code>', methods = ['GET'])
def on_qr_code_scan(code):
    flyer = get_flyer_dao_from_qr_code(sql, code)

    if flyer is None:
        return Resp.notFound(f'{code} is not a known flyer')

    if not flyer.is_registered():
        # Temp redirect into mobile app, so user can register it
        return redirect(URL_INTO_EXPO_APP % code, code=307)

    flyer.incr_hits()
    loc = flyer.get_redirect_url()

    # Permanent redirect to campaign's url
    return redirect(loc, code=301)

#
# Tags
#

@app.route('/tags/list', methods = ['GET'])
def list_tags():
    query = request.values['query'] if 'query' in request.values else ''
    tags = sql.executeGetColumn("select name from Tags where name like %s limit 50;", ['%'+query+'%'])
    return Resp.heresYourTags(tags)

@app.route('/tags/add', methods = ['POST'])
def add_tag():
    req_data = request.values
    token = req_data['token']
    tag = req_data['tag']

    org_id = auth.getOrgIdFromToken(token)

    if org_id is None:
        return Resp.unauthorized()

    tag_exists = bool(sql.count('select count(*) from Tags where name=%s;', [tag]))

    if not tag_exists:
        rv = sql.query('insert into Tags (name) values (%s);', [tag])

    tag_id = sql.firstOrNone('select (tag_id) from Tags where name=%s;', [tag])

    if not tag_id:
        raise 'wat'

    assoc_exists = bool(sql.count('select count(*) from Tags2Orgs where org_id=%s and tag_id=%s;', [org_id, tag_id]))

    if not assoc_exists:
        sql.query('insert into Tags2Orgs (org_id, tag_id) values (%s, %s);', [org_id,tag_id])

    return Resp.okNoContent()


@app.route('/tags/self', methods = ['GET'])
def get_org_tags():
    req_data = request.values
    token = req_data['token']

    org_id = auth.getOrgIdFromToken(token)

    if org_id is None:
        return Resp.unauthorized()

    print('tagssefl',org_id)

    tag_ids = sql.executeGetColumn("select tag_id from Tags2Orgs where org_id=%s", (org_id,))

    tags = []
    for tag_id in tag_ids:
        rv = sql.firstOrNone("select name from Tags where tag_id=%s", (tag_id,))
        if rv:
            tags.append(rv)

    return Resp.heresYourTags(tags)


#
# Campaigns
#

@app.route('/campaigns/new', methods = ['POST'])
def add_campaign():
    req_data = request.values
    token = req_data['token'] # string
    payload = req_data['payload'] # base64 encoded
    qr_horiz = req_data['qr_horiz'] # float
    qr_vert = req_data['qr_vert'] # float
    width = req_data['width'] # float
    height = req_data['height'] # float
    camp_name = req_data['camp_name'] # string
    dest_url = req_data['dest_url'] # string

    org_id = auth.getOrgIdFromToken(token)

    if org_id is None:
        return Resp.forbidden()

    already_exists = bool(sql.count('select count(*) from Campaigns where org_id=%s and name=%s', [org_id, camp_name]))

    if already_exists:
        return Resp.conflictResourceExists()

    q = 'insert into Campaigns (name, org_id, qr_horiz, qr_vert, width, height, dest_url) values (%s,%s,%s,%s,%s,%s,%s);'
    sql.query(q, [camp_name, org_id, qr_horiz, qr_vert, width, height, dest_url])

    # TODO: upload payload to a bucket and then later set the resource_url and thumb_url
    # - need to be able to upload... really we should be able to do this locally
    camp_id = sql.firstOrNone("select camp_id from Campaigns where org_id=%s and name=%s", [org_id, camp_name])
    if camp_id:
        f = request.files['file']
        if f:
            new_filename = "./blanks/" + str(camp_id) + ".pdf"
            print("Saving at", new_filename)
            f.save(new_filename)
            return Resp.okNoContent()


    return Resp.forbidden()

@app.route('/campaigns/list', methods = ['GET'])
def get_campaigns():
    token = request.values['token']

    org_id = auth.getOrgIdFromToken(token)

    if org_id is None:
        return Resp.forbidden()

    q = 'select camp_id, name, thumb_url, dest_url from Campaigns where org_id=%s;'

    response = [gen_campaign(*row) for row in sql.query(q, [org_id])]

    return Resp.heresYourCampaigns(response)

@app.route('/campaigns/flyers', methods = ['GET'])
def get_campaign_flyers():
    req_data = request.values
    token = req_data['token']
    camp_id = req_data['camp_id']

    org_id = auth.getOrgIdFromToken(token)

    if org_id is None:
        return Resp.forbidden()

    q = 'select flyer_id, floor_num, hits, building_id from Flyers where org_id=%s and camp_id=%s;'
    resp = sql.query(q, [org_id, camp_id])

    flyers = []

    for row in resp:
        flyer_id = row[0]
        floor_num = row[1]
        hits = row[2]
        building_id = row[3]

        building_q = 'select name from Buildings where building_id=%s limit 1;'
        building_resp = sql.query(building_q, [building_id])

        if not building_resp:
            raise 'oh no'

        building_name = building_resp[0][0]

        serialized = gen_flyer(flyer_id, building_name, floor_num, hits)
        flyers.append(serialized)

    return Resp.heresYourFlyers(flyers)

#
# HACK: no async jobs
#

def genFlyerCode(org_id, camp_id):
    code = token_hex(5)
    while sql.count("select count(*) from Flyers where code=%s", [code]) > 0:
        code = token_hex(5)
    sql.query("insert into Flyers (code, hits, camp_id, org_id) values (%s, 0, %s, %s);", [code, org_id, camp_id])
    return get_flyer_dao_from_qr_code(sql, code)

@app.route('/qr-batch', methods = ['GET'])
def get_new_qr_batch():
    res_data = request.values
    token = res_data['token']
    org_id = auth.getOrgIdFromToken(token)

    camp_id = res_data['camp_id']
    n = int(res_data['n'])
    flyers = [genFlyerCode(org_id, camp_id) for _ in range(n)]
    blank_url = './blanks/' + camp_id + '.pdf'
    print("loading from", blank_url)
    pdfqr = PDF_QR(blank_url, 0.4, 0.43, 0.2, 0.14)
    urls = [ANALYTICS_URL + a.code for a in flyers]
    pdfqr.generatePDF(urls, "./loaded/" + camp_id + ".pdf")
    return send_file('./loaded/' + camp_id + ".pdf")


#
# Jobs
# TODO: pair on this
#

# @app.route('/jobs/new', methods = ['POST'])
# def add_pdf_gen():
    # # TODO pull variables from POST
    # token = request.args.get('token')
    # num = request.args.get('n')
    # camp_id = request.args.get('camp_id')
    # # TODO add to jobs
    # task = gen_pdf.apply_async()
    # return jsonify({}), 202, {'job_id': task.id}

# @celery.task
# def gen_pdf():
    # print("Background task ran.")
    # return {"result": "task fin"}

# @app.route('/jobs/status', methods = ['GET'])
# def get_job_status():
    # token = request.args.get('token')
    # job_id = request.args.get('job_id')
    # task = gen_pdf.AsyncResult(job_id)
    # if task.state == 'PENDING':
        # return jsonify({}), 202
    # elif task.state != 'FAILURE':
        # return jsonify(task.info.get('result', 0)), 200
    # else:
        # return jsonify({}), 403


if __name__ == '__main__':
    app.run()
