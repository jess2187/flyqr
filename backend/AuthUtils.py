from SqlHelper import SqlHelper
from secrets import token_hex

class AuthUtils:
    def __init__(self, sql, bcrypt):
        self.sql = sql
        self.bcrypt = bcrypt

    def accountExists(self, email):
        q = 'select count(*) from Organizations where email=%s;'
        return self.sql.count(q, (email,)) != 0

    def createUser(self, name, email, password):
        password = password.encode('utf-8')
        db_password = self.bcrypt.generate_password_hash(password).decode('utf-8')

        q = 'insert into Organizations (name, email, password) values (%s, %s, %s);'
        self.sql.query(q, [name, email, db_password])

    def checkUser(self, email, password):
        q = 'select (password) from Organizations where email=%s;'
        db_password = self.sql.firstOrNone(q, [email])

        if not db_password:
            return False

        password = password.encode('utf-8')
        return self.bcrypt.check_password_hash(db_password, password)

    def createTokenForOrgGivenEmail(self, email):
        token = token_hex(40) # 40 byte random auth token
        
        org_id = self._getOrgIdFromEmail(email)

        if org_id is None:
            raise 'unlucky :('

        q = 'insert into AuthTokens (token, org_id) values (%s, %s);'
        self.sql.query(q, [token, org_id])

        return token

    def _getOrgIdFromEmail(self, email):
        q = 'select org_id from Organizations where email=%s;'
        return self.sql.firstOrNone(q, [email])

    def getOrgIdFromToken(self, token):
        q = 'select org_id from AuthTokens where token=%s;'
        return self.sql.firstOrNone(q, [token])

    def deleteToken(self, token):
        q = 'delete from AuthTokens where token=%s;'
        self.sql.query(q, [token])
