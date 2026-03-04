-- Writes a script that lists records with a score greater than or equal to 10 ordered by score descending
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;