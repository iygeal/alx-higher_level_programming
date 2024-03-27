-- This script creates a database named hbtn_0d_2 and a user named user_0d_2.
-- It grants the user SELECT privilege on the database.
-- The script handles cases where the database or user might already exist.

-- Create database hbtn_0d_2 if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user user_0d_2 with password user_0d_2_pwd if it doesn't exist
CREATE USER IF NOT EXISTS user_0d_2@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege on hbtn_0d_2 to user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@'localhost';
