
-- Table structure for table `contacts`

DROP TABLE IF EXISTS `contacts`;

CREATE TABLE `contacts` (
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` varchar(200) NOT NULL,
  `message` varchar(300) NOT NULL,
  `contact_date` datetime DEFAULT NULL,
  PRIMARY KEY (`first_name`,`last_name`,`email`,`message`)
) 


--Insert Query
INSERT INTO `contacts` VALUES ('Tom','Sagi','tomsag@post.bgu.ac.il','How fast is the delivery?','2022-01-01 00:00:00'),('Alon','Halevi','alonha@post.bgu.ac.il','Hey , could you contact me on my phone number?','2022-01-01 00:00:00');