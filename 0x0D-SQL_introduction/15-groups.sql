-- script lists number of records with the same score
SELECT score, COUNT(*) AS number
from second_table
GROUP BY score
ORDER BY number DESC;
