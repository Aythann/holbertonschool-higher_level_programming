-- Writes a script that lists all records where the name column is not NULL ordered by score descending
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;