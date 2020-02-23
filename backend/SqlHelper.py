from flask import jsonify
from flask_mysqldb import MySQL

class SqlHelper:
    def __init__(self, app):
        self.mysql = MySQL(app)

    def query(self, preparedQuery, values):
        cur = self.mysql.connection.cursor()
        cur.execute(preparedQuery, values)
        rv = cur.fetchall()
        cur.close()
        return rv

    def execute(self, statement):
        cur = self.mysql.connection.cursor()
        cur.execute(statement)
        rv = cur.fetchall()
        cur.close()
        return rv

    def executeGetColumn(self, statement):
        return [e[0] for e in self.execute(statement)]

    def json(self, preparedQuery, values):
        return jsonify(self.query(preparedQuery, values))

    def count(self, statement, values):
        return self.query(statement, values)[0][0]
