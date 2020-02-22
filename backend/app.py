from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
import config
from objects import gen_organization, gen_campaign, gen_flyer

app = Flask(__name__)

app.config['MYSQL_HOST'] = config.host
app.config['MYSQL_USER'] = config.user
app.config['MYSQL_PASSWORD'] = config.passwd
app.config['MYSQL_DB'] = config.db
mysql = MySQL(app)

@app.route('/ping')
def ping():
    return "pong"


@app.route('/orgs', methods = ['GET'])
def orgs():
    cur = mysql.connection.cursor()
    cur.execute("show tables;")
    rv = cur.fetchall()
    cur.close()
    return jsonify(rv)

#
# Authentication
#
@app.route('/auth/register', methods = ['POST'])
def register_org():
    email = ""
    password = ""
    # TODO

@app.route('/auth/login', methods = ['POST'])
def login_org():
    email = ""
    password = ""
    # TODO

@app.route('/auth/logout', methods = ['POST'])
def logout_org():
    token = ""
    #TODO

#
# Analytics
#

@app.route('/x/<flyer_code>', methods = ['GET'])
def addHit(flyer_code):
    # TODO add hit to DB
    # TODO redirect

#
# Tags
#

@app.route('/tags/list', methods = ['GET'])
def list_tags():
    # TODO return all tags in db

@app.route('/tags/add', methods = ['POST'])
def add_tag():
    # TODO get vars from POST
    token = ""
    tag = ""
    # TODO insert tag into DB

@app.route('/tags/self', methods = ['GET'])
def get_org_tags():
    token = request.args.get('token')
    # TODO get org tags associated w/ token

#
# Campaigns
#

@app.route('/campaigns/new', methods = ['POST'])
def add_campaign():
    token = request.args.get('token')
    payload = request.args.get('payload')
    qr_horiz = request.args.get('qr_horiz')
    qr_vert = request.args.get('qr_vert')
    width = request.args.get('width')
    height = request.args.get('height')
    camp_name = request.args.get('camp_name')
    dest_url = request.args.get('dest_url')
    print("Received: " + token)

@app.route('/campaigns/list', methods = ['GET'])
def get_campaigns():
    token = request.args.get('token')
    camps = [] # TODO use SQL call to get list
    resp = []
    for camp in camps:
        # TODO load vars into gen_campaign
        camp_json = gen_campaign(id, name, thumb_url, dest_url)
        resp.append(camp_json)
    return jsonify(resp)

@app.route('/campaigns/flyers', methods = ['GET'])
def get_campaign_flyers():
    token = request.args.get('token')
    camp_id = request.args.get('camp_id')
    camp_flyers = [] # TODO use SQL call to get list
    resp = []
    for flyer in camp_flyers:
        # TODO load vars into gen_flyer
        flyer_json = gen_flyer(id, building_name, floor_num, hits)
        resp.append(flyer_json)
    return jsonify(resp)


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

@app.route('/jobs/status', methods = ['GET'])
def get_job_status():
    token = request.args.get('token')
    job_id = request.args.get('job_id')
    # TODO SQL and return stuff


if __name__ == '__main__':
    app.run()