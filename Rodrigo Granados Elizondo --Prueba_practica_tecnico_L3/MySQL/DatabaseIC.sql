-- MySQL Workbench Forward Engineering
use db;

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema prueba_istmocenter
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema prueba_istmocenter
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `prueba_istmocenter` DEFAULT CHARACTER SET utf8 ;
USE `prueba_istmocenter` ;

-- -----------------------------------------------------
-- Table `prueba_istmocenter`.`PANELPERSONS`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `prueba_istmocenter`.`PANELPERSONS` (
  `PERSON_ID` INT NOT NULL AUTO_INCREMENT,
  `PERSON_NAME` VARCHAR(45) NULL,
  `PERSON_EMAIL` VARCHAR(300) NULL,
  `PERSON_PASSWORD` VARCHAR(100) NULL,
  PRIMARY KEY (`PERSON_ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `prueba_istmocenter`.`PANELINVENTORY`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `prueba_istmocenter`.`PANELINVENTORY` (
  `ITEM_ID` INT NOT NULL AUTO_INCREMENT,
  `ITEM_BARCODE` VARCHAR(100) NULL,
  `CREATED` VARCHAR(45) NULL,
  `CREATED_BY` INT NOT NULL,
  INDEX `fk_PANEL-INVENTORY_PANEL-PERSONS_idx` (`CREATED_BY` ASC) VISIBLE,
  PRIMARY KEY (`ITEM_ID`),
  CONSTRAINT `fk_PANEL-INVENTORY_PANEL-PERSONS`
    FOREIGN KEY (`CREATED_BY`)
    REFERENCES `prueba_istmocenter`.`PANELPERSONS` (`PERSON_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
