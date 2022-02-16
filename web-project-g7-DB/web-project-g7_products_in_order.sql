
-- Table structure for table `products_in_order`


DROP TABLE IF EXISTS `products_in_order`;

CREATE TABLE `products_in_order` (
  `orderID` int NOT NULL,
  `productID` int NOT NULL,
  `quantity` int NOT NULL,
  `total_price` double DEFAULT NULL,
  PRIMARY KEY (`orderID`,`productID`),
  CONSTRAINT `FK_productID` FOREIGN KEY (`productID`) REFERENCES `products` (`productID`),
  CONSTRAINT `FK_orderID` FOREIGN KEY (`orderID`) REFERENCES `orders` (`orderID`)
) 

--Insert Query

INSERT INTO `products_in_order` VALUES (2,1,1,20),(3,2,1,30),(4,1,1,20),(4,2,1,30);