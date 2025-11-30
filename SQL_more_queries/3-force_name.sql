#!/bin/bash
# Script to create the table 'force_name' in a given MySQL database.
# Usage: ./create_force_name.sh database_name
# This script will not fail if the table already exists.
# Demonstrates inserts depending on table existence.

DB_NAME=$1

# Connect to MySQL and create the table if it does not exist
mysql -u root -p -D "$DB_NAME" -e "
-- Create the table 'force_name' if it does not exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
"

# Demonstration of regular insert (should succeed)
mysql -u root -p -D "$DB_NAME" -e "
INSERT INTO force_name (id, name) VALUES (1, 'Jedi');
"

# Attempt insert without a name (should fail because 'name' is NOT NULL)
mysql -u root -p -D "$DB_NAME" -e "
INSERT INTO force_name (id) VALUES (2);
"
