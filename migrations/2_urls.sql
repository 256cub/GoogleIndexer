
-- -----------------------------------------------------
-- Table `urls`
-- -----------------------------------------------------
SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS `urls`;
SET FOREIGN_KEY_CHECKS = 1;

CREATE TABLE `urls` (
    `id`                    INT NOT NULL AUTO_INCREMENT,
    `websites_id`           INT(11) DEFAULT NULL,
    `url`                   VARCHAR(255) DEFAULT NULL,
    `indexed`               TINYINT(1) DEFAULT NULL,
    `status`                ENUM('PENDING', 'ACTIVE', 'INACTIVE', 'BLOCKED', 'ERROR') DEFAULT NULL,
    `date_updated`          DATETIME DEFAULT NULL,
    `date_created`          DATETIME DEFAULT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `name` (`url`) USING BTREE
) ENGINE=InnoDB;

DROP TRIGGER IF EXISTS `urls_BEFORE_INSERT`;
CREATE TRIGGER `urls_create` BEFORE INSERT ON `urls` FOR EACH ROW SET NEW.date_created = NOW();

DROP TRIGGER IF EXISTS `urls_BEFORE_UPDATE`;
CREATE TRIGGER `urls_update` BEFORE UPDATE ON `urls` FOR EACH ROW SET NEW.date_updated = NOW();
