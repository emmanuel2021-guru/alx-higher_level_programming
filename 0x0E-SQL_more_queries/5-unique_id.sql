-- This script creates the table 'unique_id' on a MySQL server with a unique column
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
