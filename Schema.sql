-- -----------------------------------------------------
-- Applicant name: Zarko Milojevic
-- Email: zarkomilojevic@yahoo.com
-- Company: PM Accelerator
-- Technical Assessment
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Create Schema and User
-- -----------------------------------------------------
-- DROP SCHEMA IF EXISTS `weatherapp`;
-- CREATE SCHEMA IF NOT EXISTS `weatherapp`;
-- DROP USER IF EXISTS `weatheruser`@`localhost`;
-- CREATE USER IF NOT EXISTS 'weatheruser'@'localhost' IDENTIFIED BY '1234';
-- GRANT ALL PRIVILEGES ON `weatherapp`.* TO 'weatheruser'@'localhost';

-- -----------------------------------------------------
-- Student name: Zarko Milojevic
-- Create Table `WeatherData`.`weatherapp`
-- -----------------------------------------------------
-- USE `weatherapp`;
-- DROP TABLE IF EXISTS `WeatherData`;

-- Create a table to store values
/*
CREATE TABLE WeatherData (
    id INT AUTO_INCREMENT PRIMARY KEY,
    location VARCHAR(255),
    latitude FLOAT,
    longitude FLOAT,
    weather_condition VARCHAR(255),
    temperature FLOAT,
    humidity INT,
    wind_speed FLOAT,
    date_range VARCHAR(255),
    date_requested DATETIME DEFAULT CURRENT_TIMESTAMP
);
*/
-- SELECT * FROM WeatherData;


