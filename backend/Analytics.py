from FlyerDAO import FlyerDAO

class Analytics:
    def __init__(self, sql):
        self.sql = sql

    def get_flyer_from_code(self, code):
        q = 'select (flyer_id) from Flyers where code=%s'
        vs = (code,)
