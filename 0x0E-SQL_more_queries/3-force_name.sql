-- This script creates a table named force_name in a MySQL database
-- The force_name table has two columns: id and name
-- The id column is of type INT
-- The name column is of type VARCHAR(256) and cannot be null
-- The script handles the edge case where the table force_name already exists

CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);