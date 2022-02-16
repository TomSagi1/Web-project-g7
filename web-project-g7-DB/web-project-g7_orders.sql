
-- Table structure for table `orders`

DROP TABLE IF EXISTS `orders`;

CREATE TABLE `orders` (
  `orderID` int NOT NULL,
  `order_date` datetime DEFAULT NULL,
  `total_price` double DEFAULT NULL,
  `customerID` int DEFAULT NULL,
  `approved` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`orderID`),
  CONSTRAINT `FK_customer` FOREIGN KEY (`customerID`) REFERENCES `customers` (`customerID`)
) 


-- Insert Query

INSERT INTO `orders` VALUES (1,'2022-01-01 00:00:00',100,1,NULL),(2,'2022-01-01 00:00:00',70,1,NULL);