-- phpMyAdmin SQL Dump -- version 5.2.1 -- https://www.phpmyadmin.net/ -- -- Host: 127.0.0.1 -- Generation Time: Oct 02, 2024 at 09:17 AM -- Server version: 10.4.32-MariaDB -- PHP Version: 8.2.12 
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO"; START 
TRANSACTION; 
SET time_zone = "+00:00"; 
/*!40101 
@OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */; 
/*!40101 
SET 
SET 
@OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */; 
/*!40101 
@OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */; 
/*!40101 SET NAMES utf8mb4 */; 
SET 
41 
-- -- Database: voiceback -- -- -- Table structure for table admin -- 
CREATE TABLE admin ( id 
int(11) NOT NULL, 
role varchar(11) NOT NULL, username 
varchar(10) NOT NULL, password 
varchar(10) NOT NULL 
) 
ENGINE=InnoDB 
COLLATE=utf8mb4_general_ci; -- -- Dumping data for table admin -- 
DEFAULT 
CHARSET=utf8mb4 
INSERT INTO admin (id, role, username, password) VALUES (1, 
'admin', 'admin', 'admin'); 
42 
-- -- Table structure for table user -- 
CREATE TABLE user ( 
account_no int(11) NOT NULL, username 
varchar(10) NOT NULL, password 
varchar(10) NOT NULL, role varchar(10) 
NOT NULL, mobile varchar(10) NOT 
NULL, 
account_balance varchar(10) NOT NULL 
) 
ENGINE=InnoDB 
COLLATE=utf8mb4_general_ci; -- -- Dumping data for table user -- 
DEFAULT 
CHARSET=utf8mb4 
INSERT INTO user (account_no, username, password, role, mobile, 
account_balance) VALUES 
(1, 'admin', 'admin', 'admin', '7845127845', '5000'), 
43 
(2, 'naresh', '123', 'user', '123', '480'), 
(3, 'priya', '123', 'user', '7845127485', '900'); -- -- Indexes for dumped tables -- -- -- Indexes for table admin -- 
ALTER TABLE admin ADD 
PRIMARY KEY (id); -- -- Indexes for table user -- 
ALTER TABLE user 
ADD PRIMARY KEY (account_no); -- -- AUTO_INCREMENT for dumped tables -- -- 
44 
-- AUTO_INCREMENT for table admin -- 
ALTER TABLE admin 
MODIFY 
id 
AUTO_INCREMENT=2; -- 
int(11) -- AUTO_INCREMENT for table user -- 
ALTER TABLE user 
NOT 
NULL 
AUTO_INCREMENT, 
MODIFY account_no int(11) NOT NULL AUTO_INCREMENT, 
AUTO_INCREMENT=4; 
COMMIT; 
/*!40101 
CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;   
/*!40101  
CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;  
/*!40101 
COLLATION_CONNECTI 
ON=@OLD_COLLATION_   
CONNECTION/*  
