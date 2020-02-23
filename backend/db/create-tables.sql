-- -----------------------------------------------------
-- Table `Organizations`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Organizations` ;

CREATE TABLE IF NOT EXISTS `Organizations` (
  `org_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  `email` VARCHAR(100) NOT NULL,
  `password` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`org_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `AuthTokens`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `AuthTokens` ;

CREATE TABLE IF NOT EXISTS `AuthTokens` (
  `token` VARCHAR(200) NOT NULL,
  `org_id` INT NOT NULL,
  PRIMARY KEY (`token`),
  CONSTRAINT `fk_AuthTokens_Organizations1` FOREIGN KEY (`org_id`) REFERENCES `Organizations` (`org_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Campaigns`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Campaigns` ;

CREATE TABLE IF NOT EXISTS `Campaigns` (
  `camp_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  `resource_url` VARCHAR(200) NULL,
  `thumb_url` VARCHAR(200) NULL,
  `dest_url` VARCHAR(200) NULL,
  `org_id` INT NOT NULL,
  PRIMARY KEY (`camp_id`),
  CONSTRAINT `fk_Campaigns_Organizations1` FOREIGN KEY (`org_id`) REFERENCES `Organizations` (`org_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Tags`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Tags` ;

CREATE TABLE IF NOT EXISTS `Tags` (
  `tag_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(60) NOT NULL,
  PRIMARY KEY (`tag_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Tags2Orgs`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Tags2Orgs` ;

CREATE TABLE IF NOT EXISTS `Tags2Orgs` (
  `tag_id` INT NOT NULL,
  `org_id` INT NOT NULL,
  CONSTRAINT `fk_Tags2Orgs_Tags` FOREIGN KEY (`tag_id`) REFERENCES `Tags` (`tag_id`),
  CONSTRAINT `fk_Tags2Orgs_Organizations1` FOREIGN KEY (`org_id`) REFERENCES `Organizations` (`org_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Buildings`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Buildings` ;

CREATE TABLE IF NOT EXISTS `Buildings` (
  `building_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  `min_floor` INT NOT NULL,
  `max_floor` INT NOT NULL,
  PRIMARY KEY (`building_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Flyers`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `Flyers` ;

CREATE TABLE IF NOT EXISTS `Flyers` (
  `flyer_id` INT NOT NULL AUTO_INCREMENT,
  `floor_num` INT NULL,
  `code` VARCHAR(20) NOT NULL,
  `hits` INT NOT NULL,
  `camp_id` INT NOT NULL,
  `org_id` INT NOT NULL,
  `building_id` INT NULL,
  PRIMARY KEY (`flyer_id`),
  CONSTRAINT `fk_Flyers_Campaigns1` FOREIGN KEY (`camp_id`) REFERENCES `Campaigns` (`camp_id`),
  CONSTRAINT `fk_Flyers_Buildings1` FOREIGN KEY (`building_id`) REFERENCES `Buildings` (`building_id`)
) ENGINE = InnoDB;

