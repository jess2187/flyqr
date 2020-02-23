from SqlHelper import SqlHelper
import base64

class AuthUtils:
    def __init__(self, sql, bcrypt):
        self.sql = sql
        self.bcrypt = bcrypt

    def accountExists(self, email):
        q = 'select count(*) from Organizations where email=%s;'
        return self.sql.count(q, (email,)) != 0

    def createUser(self, name, email, password):
        bcrypted_pass = self.bcrypt.generate_password_hash(password)
        encoded_pass = str(base64.b64encode(bcrypted_pass), 'utf-8')

        q = 'insert into Organizations(name, email, password) values(%s,%s,%s);'
        vs = (name, email, encoded_pass)
        json = self.sql.json(q, vs)

        print('createUser',json)
        # TODO Finish this method

    def checkUser(self, email, password):
        q = 'select (password) from Organizations where email=%s;'
        vs = (email,)
        resp = self.sql.json(q, vs)

        print(resp)

        # TODO return true if the bcrypted
        return False

    def getOrgIdFromToken(self, token):
        q = 'select (org_id) from AuthTokens where token=%s;'
        vs = (token,)
        resp = self.sql.firstOrNone(q, vs)

        if not resp:
            return None

        return resp

    def deleteToken(self, token):
        q = 'delete from AuthTokens where token=%s;'
        vs = (token,)
        self.sql.query(q, vs)
