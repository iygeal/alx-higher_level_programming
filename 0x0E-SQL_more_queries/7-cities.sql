-- This script creates a database named hbtn_0d_usa and a table named cities in the database
-- The cities table has three columns: id, state_id, and name
-- The id column is of type INT, unique, auto-generated, cannot be null, and is the primary key
-- The state_id column is of type INT, cannot be null, and must be a FOREIGN KEY referencing the id column of the states table
-- The name column is of type VARCHAR(256) and cannot be null
-- The script handles the edge cases where the database or table already exist

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
