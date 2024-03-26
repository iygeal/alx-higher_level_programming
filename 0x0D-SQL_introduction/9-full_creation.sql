-- This script creates a table second_table in a known database
-- with descriptions id, name and score
-- It also assigns values to these descritions as shown
-- If second_table already exists, errors are suppressed
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);
INSERT INTO second_table (id, name, score)
VALUES (1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);
