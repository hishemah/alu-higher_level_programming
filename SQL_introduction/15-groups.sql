-- Lists each score with the number of records that have it, most common first
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;
