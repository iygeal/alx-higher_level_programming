-- This script creates a database named hbtn_0d_usa and a table named states in the database
-- The states table has two columns: id and name
-- The id column is of type INT, unique, auto-generated, cannot be null, and is the primary key
-- The name column is of type VARCHAR(256) and cannot be null
-- The script handles the edge cases where the database or table already exist

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
