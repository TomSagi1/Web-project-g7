
-- Table structure for table `products`

DROP TABLE IF EXISTS `products`;

CREATE TABLE `products` (
  `productID` int NOT NULL,
  `product_name` varchar(45) NOT NULL,
  `price` double NOT NULL,
  `description` varchar(250) NOT NULL,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`productID`)
) 

--Insert Query

INSERT INTO `products` VALUES (1,'Comb',20,'Comb for easy and gentle brush','catalog/media/Comb.jpg'),(2,'Hair brush',30,'Best for curly hair','catalog/media/Hair-brush.jpg'),(3,'Hair cream',50,'Get your hair nice and smoove','catalog/media/Hair-cream.jpg');