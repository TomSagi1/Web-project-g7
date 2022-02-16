
-- Table structure for table `customers`

DROP TABLE IF EXISTS `customers`;

CREATE TABLE `customers` (
  `customerID` int NOT NULL,
  `phone` varchar(45) DEFAULT NULL,
  `email` varchar(200) NOT NULL,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  PRIMARY KEY (`customerID`)
) 


--Insert Query

INSERT INTO `customers` VALUES (1,'0543645314','alon@gmail.com','alon','halevi','Aa123'),(2,'0541234567','shay@gmail.com','shay','poleg','Poleg12');