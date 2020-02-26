CREATE TABLE IF NOT EXISTS Users (
  user_id   INT          NOT NULL AUTO_INCREMENT,
  name      VARCHAR(100) NOT NULL,
  email     VARCHAR(100) NOT NULL,
  bcrypt    CHAR(100)    NOT NULL UNIQUE,
  
  PRIMARY KEY (user_id)
);

CREATE TABLE IF NOT EXISTS Organizations (
  org_id  INT          NOT NULL AUTO_INCREMENT,
  name    VARCHAR(100) NOT NULL,

  PRIMARY KEY (org_id)
);

CREATE TABLE IF NOT EXISTS Users2Orgs (
  user_id  INT NOT NULL,
  org_id   INT NOT NULL,

  CONSTRAINT fk_Users2Orgs_Users
    FOREIGN KEY (user_id) REFERENCES Users (user_id),

  CONSTRAINT fk_Users2Orgs_Organizations
    FOREIGN KEY (org_id) REFERENCES Organizations (org_id)
);

CREATE TABLE IF NOT EXISTS AuthTokens (
  token    CHAR(100) NOT NULL,
  user_id  INT       NOT NULL,
  expires  DATETIME  NOT NULL,

  PRIMARY KEY (token),

  CONSTRAINT fk_AuthTokens_Users
    FOREIGN KEY (user_id) REFERENCES Users (user_id)
);

CREATE TABLE IF NOT EXISTS QrShapes (
  shape_id  INT   NOT NULL AUTO_INCREMENT,
  rotation  FLOAT NOT NULL,
  scale     FLOAT NOT NULL,
  x         FLOAT NOT NULL,
  y         FLOAT NOT NULL,

  PRIMARY KEY (shape_id)
);

CREATE TABLE IF NOT EXISTS Campaigns (
  camp_id        INT          NOT NULL AUTO_INCREMENT,
  org_id         INT          NOT NULL,
  shape_id       INT          NOT NULL,
  name           VARCHAR(100) NOT NULL,
  dest_url       VARCHAR(200) NOT NULL,
  description    VARCHAR(300)     NULL,
  resource_url   VARCHAR(200)     NULL,
  thumbnail_url  VARCHAR(200)     NULL,

  PRIMARY KEY (camp_id),

  CONSTRAINT fk_Campaigns_Organizations
    FOREIGN KEY (org_id) REFERENCES Organizations (org_id),

  CONSTRAINT fk_Campaigns_QrShapes
    FOREIGN KEY (shape_id) REFERENCES QrShapes (shape_id)
);

CREATE TABLE IF NOT EXISTS Tags (
  tag_id  INT         NOT NULL AUTO_INCREMENT,
  name    VARCHAR(60) NOT NULL,

  PRIMARY KEY (tag_id)
);

CREATE TABLE IF NOT EXISTS Tags2Orgs (
  tag_id  INT NOT NULL,
  org_id  INT NOT NULL,

  CONSTRAINT fk_Tags2Orgs_Tags
    FOREIGN KEY (tag_id) REFERENCES Tags (tag_id),

  CONSTRAINT fk_Tags2Orgs_Organizations
    FOREIGN KEY (org_id) REFERENCES Organizations (org_id)
);

CREATE TABLE IF NOT EXISTS Buildings (
  building_id  INT          NOT NULL AUTO_INCREMENT,
  name         VARCHAR(100) NOT NULL,
  min_floor    INT          NOT NULL,
  max_floor    INT          NOT NULL,

  PRIMARY KEY (building_id)
);

CREATE TABLE IF NOT EXISTS Flyers (
  code         CHAR(20) NOT NULL,
  camp_id      INT      NOT NULL,
  org_id       INT      NOT NULL,
  hits         INT      NOT NULL,
  building_id  INT          NULL,
  floor_num    INT          NULL,

  PRIMARY KEY (code),

  CONSTRAINT fk_Flyers_Campaigns
    FOREIGN KEY (camp_id) REFERENCES Campaigns (camp_id),

  FOREIGN KEY (building_id) REFERENCES Buildings (building_id)
);
