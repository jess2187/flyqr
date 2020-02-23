_flyers = {} # TODO: lfu or lru cache instead of keeping everything...

def get_flyer_dao_from_qr_code(sql, code):
    if code in _flyers:
        return _flyers[code]

    q = 'select flyer_id from Flyers where code=%s'
    flyer_id = sql.firstOrNone(q, [code])

    if flyer_id is None:
       return None

    flyer = FlyerDAO(sql, flyer_id)
    _flyers[code] = flyer
    return flyer

class FlyerDAO:
    def __init__(self, sql, flyer_id):
        self.sql = sql
        self.flyer_id = flyer_id
        self.cached_is_registered = None
        self.cached_redirect_url = None

    def is_registered(self):
        # since we can never unregister a poster, this is ok
        if self.cached_is_registered:
            return True

        # flyers without a building_id are assumed to be unregistered
        q = 'select building_id from Flyers where flyer_id=%s;'
        self.cached_is_registered = self.sql.firstOrNone(q, [self.flyer_id]) != None
        return self.cached_is_registered

    def incr_hits(self):
        q = 'update Flyers set hits = hits + 1 where flyer_id=%s;'
        self.sql.query(q, [self.flyer_id])

    def get_redirect_url(self):
        if self.cached_redirect_url:
            return self.cached_redirect_url

        q1 = 'select camp_id from Flyers where flyer_id=%s;'
        camp_id = self.sql.firstOrNone(q1, [self.flyer_id])

        if not camp_id:
            print(f'Missing camp_id for flyer_id = {self.flyer_id}')
            return None # bruh moment

        q2 = 'select dest_url from Campaigns where camp_id=%s;'
        dest_url = self.sql.firstOrNone(q2, [camp_id])

        self.cached_redirect_url = dest_url
        return self.cached_redirect_url

    # TODO: need a register(building, floor_num) method
