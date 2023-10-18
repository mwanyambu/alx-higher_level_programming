-- script subquerries the cities table with the states table
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE states.name = 'California')
ORDER BY id ASC;
