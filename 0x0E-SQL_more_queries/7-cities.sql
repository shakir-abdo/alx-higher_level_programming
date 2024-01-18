-- create a database and create the database hbtn_0d_usa and the table cities
--  (in the database hbtn_0d_usa) in my MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use the database.
USE hbtn_0d_usa;
-- create the table.
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE AUTO_INCREMENT NOT NULL,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
PRIMARY KEY(id),
FOREIGN KEY(state_id) REFERENCES states(id));
