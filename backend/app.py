from flask import Flask, jsonify, request, redirect
from flask_api import status
from celery import Celery
import config
from objects import gen_organization, gen_campaign, gen_flyer
from SqlHelper import SqlHelper
from AuthUtils import AuthUtils
from Analytics import Analytics
from flask_bcrypt import Bcrypt
import response_utils as Resp

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
analytics = Analytics(sql)

URL_INTO_EXPO_APP = 'exp://exp.host/@evanram/flyqr?code=%s'

@app.route('/ping')
def ping():
    return "pong"

@app.route('/tables', methods = ['GET'])
def orgs():
    rv = sql.execute('show tables;')
    return Resp.okJson(rv)

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

    token = auth.checkUser(email, password)

    if not token:
        return Resp.unauthorized()

    return Resp.heresYourToken(token)

@app.route('/auth/logout', methods = ['POST'])
def logout_org(): # does not logout everywhere
    req_data = request.values
    token = req_data['token']
    
    org_id = auth.getOrdIdFromToken(token)

    if org_id is None:
        return Resp.unauthorized()

    auth.deleteToken(token)

    return Resp.okNoContent()

#
# Analytics
#

@app.route('/x/<code>', methods = ['GET'])
def on_qr_code_scan(code):
    flyer = analytics.get_flyer_from_code(code)
    
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

    return Resp.okNoContent()

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


# camp_id = request.args.get('camp_id')
# camp_flyers = [] # TODO use SQL call to get list
# resp = []
# for flyer in camp_flyers:
    # # TODO load vars into gen_flyer
    # flyer_json = gen_flyer(id, building_name, floor_num, hits)
    # resp.append(flyer_json)
# return jsonify(resp)

#
# Jobs
#

@app.route('/jobs/new', methods = ['POST'])
def add_pdf_gen():
    # TODO pull variables from POST
    token = request.args.get('token')
    num = request.args.get('n')
    camp_id = request.args.get('camp_id')
    # TODO add to jobs
    task = gen_pdf.apply_async()
    return jsonify({}), 202, {'job_id': task.id}

@celery.task
def gen_pdf():
    print("Background task ran.")
    return {"result": "task fin"}

@app.route('/jobs/status', methods = ['GET'])
def get_job_status():
    token = request.args.get('token')
    job_id = request.args.get('job_id')
    task = gen_pdf.AsyncResult(job_id)
    if task.state == 'PENDING':
        return jsonify({}), 202
    elif task.state != 'FAILURE':
        return jsonify(task.info.get('result', 0)), 200
    else:
        return jsonify({}), 403


if __name__ == '__main__':
    app.run()
