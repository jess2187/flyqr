from flask import Flask
from flask_mysqldb import MySQL
import config

app = Flask(__name__)

app.config['MYSQL_HOST'] = config.host
app.config['MYSQL_USER'] = config.user
app.config['MYSQL_PASSWORD'] = config.passwd
app.config['MYSQL_DB'] = config.db
mysql = MySQL(app)

@app.route('/ping')
def ping():
    return "pong"


@app.route('/orgs')
def orgs():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM mysql.orgs")
    rv = cur.fetchall()
    cur.close()
    return str(rv)


    

if __name__ == '__main__':
    app.run()