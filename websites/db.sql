CREATE TABLE `hotels` (
    `id` int NOT NULL AUTO_INCREMENT, `hotel_name` varchar(150) DEFAULT NULL, `hotel_location` varchar(150) DEFAULT NULL, `hotel_price` varchar(150) DEFAULT NULL, `hotel_rating` varchar(150) DEFAULT NULL, `hotel_image` varchar(150) DEFAULT NULL, `city_id` int DEFAULT NULL, PRIMARY KEY (`id`), KEY `city_id` (`city_id`), CONSTRAINT `hotels_ibfk_1` FOREIGN KEY (`city_id`) REFERENCES `cities` (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci

INSERT INTO `hotels` (`id`, `hotel_name`, `hotel_location`, `hotel_price`, `hotel_rating`, `hotel_image`) VALUES
(1, 'Hotel 1', 'Location 1', 'Price 1', 'Rating 1', 'https://images.unsplash.com/photo-1712928247899-2932f4c7dea3?q=80&w=2942&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'),
(2, 'Hotel 2', 'Location 2', 'Price 2', 'Rating 2', 'https://images.unsplash.com/photo-1712928247899-2932f4c7dea3?q=80&w=2942&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'),
(3, 'Hotel 3', 'Location 3', 'Price 3', 'Rating 3', 'https://images.unsplash.com/photo-1712928247899-2932f4c7dea3?q=80&w=2942&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'),
(4, 'Hotel 4', 'Location 4', 'Price 4', 'Rating 4', 'https://images.unsplash.com/photo-1712928247899-2932f4c7dea3?q=80&w=2942&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'),
(5, 'Hotel 5', 'Location 5', 'Price 5', 'Rating 5', 'https://images.unsplash.com/photo-1712928247899-2932f4c7dea3?q=80&w=2942&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'),
(6, 'Hotel 6', 'Location 6', 'Price 6', 'Rating 6', 'https://images.unsplash.com/photo-1712928247899-2932f4c7dea3?q=80&w=2942&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'),
(7, 'Hotel 7', 'Location 7', 'Price 7', 'Rating 7', 'https://images.unsplash.com/photo-1712928247899-2932f4c7dea3?q=80&w=2942&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'),
(8, 'Hotel 8', 'Location 8', 'Price 8', 'Rating 8', 'https://images.unsplash.com/photo-1712928247899-2932f4c7dea3?q=80&w=2942&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'),
(9, 'Hotel 9', 'Location 9', 'Price 9', 'Rating 9', 'https://images.unsplash.com/photo-1712928247899-2932f4c7dea3?q=80&w=2942&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'),
(10, 'Hotel 10', 'Location 10', 'Price 10', 'Rating 10', 'https://images.unsplash.com/photo-1712928247899-2932f4c7dea3?q=80&w=2942&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');

INSERT INTO `rooms` (`room_number`, `room_type`, `price`, `is_available`, `hotel_id`) VALUES ('1', '6', 'Single', '250', '1', '3');
INSERT INTO `rooms` (`id`, `room_number`, `room_type`, `price`, `is_available`, `hotel_id`) VALUES ('2', '21', 'Single', '300', '1', '2');
INSERT INTO `rooms` (`id`, `room_number`, `room_type`, `price`, `is_available`, `hotel_id`) VALUES ('3', '45', 'Double', '130', '1', '2');
INSERT INTO `rooms` (`id`, `room_number`, `room_type`, `price`, `is_available`, `hotel_id`) VALUES ('4', '32', 'Double', '210', '1', '1');
INSERT INTO `rooms` (`id`, `room_number`, `room_type`, `price`, `is_available`, `hotel_id`) VALUES ('5', '20', 'Single', '500', '1', '6');
INSERT INTO `rooms` (`id`, `room_number`, `room_type`, `price`, `is_available`, `hotel_id`) VALUES ('6', '11', 'Single', '320', '1', '7');
INSERT INTO `rooms` (`id`, `room_number`, `room_type`, `price`, `is_available`, `hotel_id`) VALUES ('7', '8', 'Double', '281', '1', '8');
INSERT INTO `rooms` (`id`, `room_number`, `room_type`, `price`, `is_available`, `hotel_id`) VALUES ('8', '10', 'Double', '450', '0', '4');
INSERT INTO `rooms` (`id`, `room_number`, `room_type`, `price`, `is_available`, `hotel_id`) VALUES ('9', '15', 'Single', '510', '1', '5');
INSERT INTO `rooms` (`id`, `room_number`, `room_type`, `price`, `is_available`, `hotel_id`) VALUES ('10', '5', 'Double', '421', '1', '3');

USE gotripv2;

ALTER TABLE bookings ADD COLUMN check_in_date DATETIME;
ALTER TABLE bookings ADD COLUMN check_out_date DATETIME;
SELECT * FROM `bookings`;

SELECT * FROM `rooms`;




SELECT * FROM rooms;



SELECT id FROM cities;

SELECT * FROM hotels
JOIN cities ON hotels.city_id = cities.id;

UPDATE hotels 
SET hotel_image = 'https://images.unsplash.com/photo-1455587734955-081b22074882?q=80&w=1920&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D';

UPDATE hotels SET hotel_image = 'https://images.unsplash.com/photo-1551918120-9739cb430c6d?q=80&w=2787&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' WHERE id = 1;

UPDATE hotels SET city_id = 1 WHERE id = 1;
UPDATE hotels SET city_id = 4 WHERE id = 9;
UPDATE hotels SET city_id = 8 WHERE id = 2;

UPDATE hotels 
SET name = 'new_hotel_name' 
WHERE id = 1;
-- and so on for each hotel

SELECT * FROM cities;

INSERT INTO cities (name) VALUES ('City 1'), ('City 2'), ('City 3'), ('City 4'), ('City 5'), ('City 6'), ('City 7'), ('City 8'), ('City 9'), ('City 10');

UPDATE hotels SET city_id = 1 WHERE id = 1;
UPDATE hotels SET city_id = 2 WHERE id = 7;
UPDATE hotels SET city_id = 3 WHERE id = 8;
-- and so on for each hotel

UPDATE hotels SET hotel_name = 'Hotel 1', hotel_location = 'Location 1', hotel_price = 'Price 1', hotel_rating = 'Rating 1', hotel_image = 'https://images.unsplash.com/photo-1712928247899-2932f4c7dea3?q=80&w=2942&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', city_id = 1 WHERE id = 1;