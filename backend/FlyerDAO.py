class FlyerDAO:
    def __init__(self, sql, flyer_id):
        self.sql = sql
        self.flyer_id = flyer_id

    def is_registered(self):
        return False # TODO

    def incr_hits(self):
        q = 'update Flyers set hits = hits + 1 where flyer_id=%s'
        vs = (self.flyer_id,)
        sql.query(q, vs)
        return # TODO

    def get_redirect_url(self):
        return 'https://example.com'

    # TODO: need a register(building, floor_num) method
