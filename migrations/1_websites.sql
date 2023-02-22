
-- -----------------------------------------------------
-- Table `websites`
-- -----------------------------------------------------
SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS `websites`;
SET FOREIGN_KEY_CHECKS = 1;

CREATE TABLE `websites` (
    `id`                    INT NOT NULL AUTO_INCREMENT,
    `name`                  VARCHAR(255) DEFAULT NULL,
    `url`                   VARCHAR(255) DEFAULT NULL,
    `indexed`               TINYINT(1) DEFAULT NULL,
    `status`                ENUM('PENDING', 'ACTIVE', 'INACTIVE', 'BLOCKED', 'ERROR') DEFAULT NULL,
    `date_updated`          DATETIME DEFAULT NULL,
    `date_created`          DATETIME DEFAULT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `name` (`url`) USING BTREE
) ENGINE=InnoDB;

DROP TRIGGER IF EXISTS `websites_BEFORE_INSERT`;
CREATE TRIGGER `websites_create` BEFORE INSERT ON `websites` FOR EACH ROW SET NEW.date_created = NOW();

DROP TRIGGER IF EXISTS `websites_BEFORE_UPDATE`;
CREATE TRIGGER `websites_update` BEFORE UPDATE ON `websites` FOR EACH ROW SET NEW.date_updated = NOW();
