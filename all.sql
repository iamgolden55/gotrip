CREATE TABLE `city_db` (
  `city_id` int NOT NULL AUTO_INCREMENT,
  `city_name` varchar(100) NOT NULL,
  PRIMARY KEY (`city_id`)
);

CREATE TABLE `hotel_db` (
  `hotel_id` int NOT NULL AUTO_INCREMENT,
  `hotel_name` varchar(100) NOT NULL,
  `location` varchar(100) NOT NULL,
  `city_id` int NOT NULL,
  `image_url` varchar(255) DEFAULT NULL,
  `room_id` int DEFAULT NULL,
  PRIMARY KEY (`hotel_id`),
  KEY `city_id` (`city_id`),
  KEY `room_id` (`room_id`),
  CONSTRAINT `hotel_db_ibfk_1` FOREIGN KEY (`city_id`) REFERENCES `city_db` (`city_id`),
  CONSTRAINT `hotel_db_ibfk_2` FOREIGN KEY (`room_id`) REFERENCES `room_db` (`room_id`)
);

CREATE TABLE `payment_db` (
  `payment_id` int NOT NULL AUTO_INCREMENT,
  `reservation_id` int NOT NULL,
  `payment_amount` float NOT NULL,
  `payment_date` datetime NOT NULL,
  PRIMARY KEY (`payment_id`),
  KEY `reservation_id` (`reservation_id`),
  CONSTRAINT `payment_db_ibfk_1` FOREIGN KEY (`reservation_id`) REFERENCES `reservation_db` (`reservation_id`)
);

CREATE TABLE `reservation_db` (
  `reservation_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `room_id` int NOT NULL,
  `check_in_date` date NOT NULL,
  `check_out_date` date NOT NULL,
  `total_price` float NOT NULL,
  PRIMARY KEY (`reservation_id`),
  KEY `user_id` (`user_id`),
  KEY `room_id` (`room_id`),
  CONSTRAINT `reservation_db_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user_db` (`user_id`),
  CONSTRAINT `reservation_db_ibfk_2` FOREIGN KEY (`room_id`) REFERENCES `room_db` (`room_id`)
);

CREATE TABLE `room_db` (
  `room_id` int NOT NULL AUTO_INCREMENT,
  `hotel_id` int NOT NULL,
  `room_capacity` int NOT NULL,
  `room_type` varchar(100) NOT NULL,
  `room_price` float NOT NULL,
  `availability` tinyint(1) NOT NULL DEFAULT '1',
  `image_url` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`room_id`),
  KEY `fk_hotel_id` (`hotel_id`),
  CONSTRAINT `fk_hotel_id` FOREIGN KEY (`hotel_id`) REFERENCES `hotel_db` (`hotel_id`),
  CONSTRAINT `room_db_ibfk_1` FOREIGN KEY (`hotel_id`) REFERENCES `Hotel_db` (`hotel_id`)
);

CREATE TABLE `user_db` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `email_address` varchar(100) NOT NULL,
  `full_name` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `city` varchar(100) DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `email_address` (`email_address`),
  UNIQUE KEY `username` (`username`)
);

INSERT INTO `user_db` VALUES (1,'fessler','fessler@gmail.com','John Doe','password','London','1990-01-01'),(2,'golden','golden@gmail.com','Jane Doe','password','Manchester','1990-01-01'),(3,'test','test@test.com','John Smith','password','Bristol','1990-01-01'),(4,'jackhalloew','jackhalloew@yahoo.com','Jane Smith','password','Glasgow','1990-01-01'),(5,'goee','goee@hotmail.com','John Doe','password','Edinburgh','1990-01-01');

INSERT INTO `room_db` VALUES (1,1,2,'Single',100,1,'https://www.hilton.com/en/hotels/londondowntown-hilton-london-bankside/'),(2,1,4,'Double',150,1,'https://www.hilton.com/en/hotels/londondowntown-hilton-london-bankside/'),(3,1,6,'Family',200,1,'https://www.hilton.com/en/hotels/londondowntown-hilton-london-bankside/'),(4,2,2,'Single',100,1,'https://www.marriott'),(5,2,4,'Double',150,1,'https://www.marriott'),(6,2,6,'Family',200,1,'https://www.marriott'),(7,3,2,'Single',100,1,'https://www.ihg.com/holidayinn/hotels/us/en/bristol/brscc/hoteldetail'),(8,3,4,'Double',150,1,'https://www.ihg.com/holidayinn/hotels/us/en/bristol/brscc/hoteldetail'),(9,3,6,'Family',200,1,'https://www.ihg.com/holidayinn/hotels/us/en/bristol/brscc/hoteldetail'),(10,4,2,'Single',100,1,'https://www.radissonhotels.com/en-us/hotels/radisson-blu-glasgow'),(11,4,4,'Double',150,1,'https://www.radissonhotels.com/en-us/hotels/radisson-blu-glasgow'),(12,4,6,'Family',200,1,'https://www.radissonhotels.com/en-us/hotels/radisson-blu-glasgow'),(13,5,2,'Single',100,1,'https://www.roccofortehotels.com/hotels-and-resorts/the-balmoral-hotel/'),(14,5,4,'Double',150,1,'https://www.roccofortehotels.com/hotels-and-resorts/the-balmoral-hotel/'),(15,5,6,'Family',200,1,'https://www.roccofortehotels.com/hotels-and-resorts/the-balmoral-hotel/'),(16,6,2,'Single',100,1,'https://www.grandbrighton.co.uk/'),(17,6,4,'Double',150,1,'https://www.grandbrighton.co.uk/'),(18,6,6,'Family',200,1,'https://www.grandbrighton.co.uk/');

INSERT INTO `hotel_db` VALUES (1,'Hilton Hotel','London',7,'https://www.hilton.com/en/hotels/londondowntown-hilton-london-bankside/',1),(2,'Marriott Hotel','Manchester',8,'https://www.marriott.com/hotels/travel/manbr-manchester-marriott-victoria-and-albert-hotel/',4),(3,'Holiday Inn','Bristol',4,'https://www.ihg.com/holidayinn/hotels/us/en/bristol/brscc/hoteldetail',5),(4,'Radisson Blu','Glasgow',6,'https://www.radissonhotels.com/en-us/hotels/radisson-blu-glasgow',2),(5,'The Balmoral','Edinburgh',5,'https://www.roccofortehotels.com/hotels-and-resorts/the-balmoral-hotel/',1),(6,'The Grand','Brighton',9,'https://www.grandbrighton.co.uk/',6),(7,'The Grand','Brighton',9,'https://www.grandbrighton.co.uk/',8),(8,'The Grand','Brighton',9,'https://www.grandbrighton.co.uk/',9),(9,'The Grand','Brighton',9,'https://www.grandbrighton.co.uk/',7),(10,'The Grand','Brighton',9,'https://www.grandbrighton.co.uk/',5);

INSERT INTO `city_db` VALUES (1,'Aberdeen'),(2,'Belfast'),(3,'Birmingham'),(4,'Bristol'),(5,'Cardiff'),(6,'Edinburgh'),(7,'Glasgow'),(8,'London'),(9,'Manchester'),(10,'New Castel'),(11,'Norwich'),(12,'Nottingham'),(13,'Oxford'),(14,'Plymouth'),(15,'Swansea'),(16,'Bournemouth'),(17,'Kent');

SELECT * FROM room_db;

USE world_hotels;