-- This script creates a table named unique_id in a MySQL database
-- The unique_id table has two columns: id and name
-- The id column is of type INT with a default value of 1 and must be unique
-- The name column is of type VARCHAR(256)
-- The script handles the edge case where the table unique_id already exists

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);