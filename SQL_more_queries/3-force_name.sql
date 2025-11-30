-- Create the table 'force_name' if it does not exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);

-- Regular inserts
INSERT INTO force_name (id, name) VALUES (1, 'Holberton School');
INSERT INTO force_name (id, name) VALUES (1, 'Python is cool');
INSERT INTO force_name (id, name) VALUES (2, 'Holberton');
INSERT INTO force_name (id, name) VALUES (3, 'School');
INSERT INTO force_name (id, name) VALUES (4, 'C is fun');
