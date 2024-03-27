-- This scripts creates a server user named user_0d_1
-- It gives the user all privileges on the server
-- It then sets its password to user_0d_1_pwd
-- The script covers the edge case of whether the username already
-- exists, in which case the script still runs with no error.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';