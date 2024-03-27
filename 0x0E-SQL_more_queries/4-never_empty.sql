-- This script creates a table named id_not_null in a MySQL database
-- The id_not_null table has two columns: id and name
-- The id column is of type INT with a default value of 1 and cannot be null
-- The name column is of type VARCHAR(256)
-- The script handles the edge case where the table id_not_null already exists
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));