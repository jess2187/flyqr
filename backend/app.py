from flask import Flask
from flask_mysqldb import MySQL
import config

app = Flask(__name__)
mysql = MySQL(app)

@app.route('/ping')
def ping():
    return "pong"


@app.route('/orgs')
def orgs():
    cur, conn = getDBConnection()
    cur.execute("SELECT * FROM mysql.orgs")
    rv = cur.fetchall()
    return str(rv)

def getDBConnection():
    conn = mysql.connect(host=config.host,
                        user = config.user,
                        passwd = config.passwd,
                        db = config.db)
    return conn.cursor(), conn
    

if __name__ == '__main__':
    app.run()