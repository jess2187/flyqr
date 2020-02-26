INSERT INTO Users (user_id, name, email, bcrypt) VALUES
  (1,  'Snoopy',    'snoopy@example.com',   '$2b$12$v57YlnboMP2g02AjqspFXu.TMuRmreSIj/UdthPesPJtKI8S1h2s.' /* 'password' */),
  (2,  'C. Brown',  'c.brown@example.com',  '$2b$12$653KjtwsuYIlARcCK8GWj.4aLHT0/ZF41b5xfn/xdCFVQoCcObzGO' /* 'different-password' */);

INSERT INTO Organizations (org_id, name) VALUES
  (1,  'Peanut Club'),
  (2,  'X-Mas Tree Co.');

INSERT INTO Users2Orgs (user_id, org_id) VALUES
  (1,  1), /* Snoopy belongs to Peanut Club */
  (2,  1), /* C. Brown belongs to Peanut Club */
  (2,  2); /* C. Brown belongs to X-Mas Tree Co. */

INSERT INTO AuthTokens (token, user_id, expires) VALUES
  ('snoopy_token',          1,  NOW() + INTERVAL 10 YEAR),
  ('snoopy_token2',         1,  NOW() + INTERVAL 10 YEAR),
  ('snoopy_token_expired',  1,  NOW() - INTERVAL 10 YEAR);
  /* Purposefully not giving token to C. Brown so we can test auth w/o token */

INSERT INTO QrShapes VALUES
  /* TODO: super arbitrary... when I end up making fake assets, let's change
   * these to reflect real qr code locations on posters */
  (1,  0.0,  2.5,  33.33,  85.6),
  (2, 90.0,  1.0,     10,    10);

INSERT INTO Campaigns (camp_id, org_id, shape_id, name, dest_url, description, resource_url, thumbnail_url) VALUES
  /* TODO: real resource_url and thumbnail_url assets should be provided at some
   * point... Maybe track in git then link to github assets? */
  (1,  1,  1,  'Peanut Fest 2020',  'https://example.com/?peanut-fest-2020' /* TODO fake landing page? */,  'The biggest festival yet.',            NULL,  NULL),
  (2,  1,  2,  'Peanut Fest 2021',  'https://example.com/?peanut-fest-2021' /* TODO fake landing page? */,  'Even bigger this year..!',             NULL,  NULL),
  (3,  2,  2,  'Winter Tree Push',  'https://example.com/?winter-tree-push' /* TODO fake landing page? */,  'We really need to sell these trees!',  NULL,  NULL);

INSERT INTO Tags (tag_id, name) VALUES
  (1, 'tree-huggers'),
  (2, 'co-ed'),
  (3, 'education'),
  (4, 'dogs-welcome'),
  (5, 'no-dogs-allowed-or-birds'),
  (6, 'fun');

INSERT INTO Tags2Orgs (org_id, tag_id) VALUES
  /* Peanut Club's tags */
  (1, 2), (1, 3), (1, 4),
  /* X-Mas Tree Co.'s tags */
  (2, 1), (2, 4);

INSERT INTO Buildings (building_id, name, min_floor, max_floor) VALUES
  (1,  'Dog House',      -2,  2),
  (2,  'The School',     -1,  7),
  (3,  'Tree Lot',        0,  1),
  (4,  'Shopping Mall',   0,  2),
  (5,  'Pumpkin Patch',   0,  1);

/* In prod, code should be a random string. Not predictable / identifying. */
INSERT INTO Flyers (code, camp_id, hits, building_id, floor_num) VALUES
  /* Simple posters, nothing special */
  ('pfest20-1',  1, 41,  1,   1),
  ('pfest20-2',  1, 0,   2,  -1),
  ('pfest20-3',  1, 16,  2,   0),

  /* Hits in normal dist w/ mu=25, sigma=25 (np.random.normal) */
  ('pfest21-1',   2, 38,   2,  -1),
  ('pfest21-2',   2, 23,   2,   0),
  ('pfest21-3',   2, 74,   2,   1),
  ('pfest21-4',   2, 61,   2,   2),
  ('pfest21-5',   2, 33,   2,   3),
  ('pfest21-6',   2, 63,   2,   4),
  ('pfest21-7',   2, 46,   2,   5),
  ('pfest21-8',   2,  8,   2,   6),
  ('pfest21-9',   2, 44,   2,   7),
  ('pfest21-10',  2, 69,   2,   8),

  /* Both registered & unregistered posters */
  ('wtpush-1',   3, 12,     3,  0),
  ('wtpush-2',   3,  4,     5,  0),
  ('wtpush-X1',  3,  0,  NULL,  0),
  ('wtpush-X2',  3,  0,  NULL,  0);
