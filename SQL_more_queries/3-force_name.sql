#!/bin/bash
# Usage: ./create_force_name.sh database_name

DB_NAME=$1

mysql -u root -p -D "$DB_NAME" -e "
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
