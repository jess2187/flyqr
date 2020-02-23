insert into Organizations (org_id, name, email, password) values
  (1, 'Gaming Club',                   'gaming@colorado.edu',          '$2b$12$v57YlnboMP2g02AjqspFXu.TMuRmreSIj/UdthPesPJtKI8S1h2s.'), /* 'password' */
  (2, 'Competitive Programming Club',  'comp.prog@colorado.edu',       '$2b$12$653KjtwsuYIlARcCK8GWj.4aLHT0/ZF41b5xfn/xdCFVQoCcObzGO'), /* 'different-password' */
  (3, 'Truck Club',                    'walter.clements@gmail.com',    '$2b$12$L5nPCrO3eMvz4fn/QqnUzeeObiPeeBSeaoxU47vwwouLwMD5Vwule'), /* 'mostertruck' */
  (4, 'Robert Downey Jr Fan Club',     'stuff@colorado.edu',           '$2b$12$lirjEH9y17wj9P6/BgzqY.nkki3biXToZq3X4wKze7k6/x1r4FpwC'); /* 'imstuff' */

insert into Buildings (building_id, name, min_floor, max_floor) values
  (1, 'Duane Physics',       -2, 2),
  (2, 'Engineering Center',  -1, 8),
  (3, 'Baker Hall',          -1, 4),
  (4, 'Lesser House',         1, 2),
  (5, 'UMC',                 -2, 5);

insert into Campaigns (camp_id, name, resource_url, thumb_url, dest_url, org_id) values
  (1, 'Fall Recruitment',   'https://example.com/poster.pdf',           'https://example.com/thumb.png',        'https://example.com/join-gaming-club',     1),
  (2, 'Spring Recruitment', 'https://example.com/spring-poster.pdf',    'https://example.com/spring-thumb.png', 'https://example.com/join-gaming-club-2',   1),
  (3, 'Truck Ralley 2020',  'https://example.com/truck-rally-2020.pdf', 'https://example.com/rally2020.png',    'https://example.com/truckRally2020BooYah', 3);

insert into Tags (tag_id, name) values
  (1, 'gamers-welcome'),
  (2, 'co-ed'),
  (3, 'educational'),
  (4, 'trucks'),
  (5, 'math'),
  (6, 'engineering'),
  (7, 'reading');

insert into Tags2Orgs (org_id, tag_id) values
  (1, 1), (1, 2), (1, 6),              /* Gaming Club */
  (2, 3), (2, 5), (2, 6), (2, 2),      /* Competitive Programming Club */
  (3, 4), (3, 6), (3, 2),              /* Truck Club */
  (4, 7), (4, 2);                      /* RDJr Fan Club */

/* b/c I'm lazy, all flyers are for Gaming Club in Duane (+ 1 unreg'd poster). */
insert into Flyers (flyer_id, floor_num, code, hits, camp_id, org_id, building_id) values
  (1,    1, 'f1r5tc0d3', 53, 1, 1,    1),
  (2,    2, 's3c0nd0n3', 14, 1, 1,    1),
  (3,   -1, 'th1rdc0d3',  2, 1, 1,    1),
  (4, NULL, 'unregd',     0, 1, 1, NULL);

insert into AuthTokens (org_id, token) values
  (1, 'sup3rs3cur34utht0k3n'); /* Log into Gaming Club with this token */
