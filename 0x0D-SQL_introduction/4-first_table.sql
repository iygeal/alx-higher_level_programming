-- This script creates a table named first_table in current database
-- first_name table has these descriptions:
-- id INT
-- name VARCHAR(256) - 256 characters max
-- If first_table already exists, this script won't fail
CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));