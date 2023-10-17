-- script creates second_table in hbtn_0c_0 database
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
);

-- create records
INSERT INTO hbtn_0c_0.second_table (id, name, score)
VALUES (1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);