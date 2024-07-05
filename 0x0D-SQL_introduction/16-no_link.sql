-- This script lists all records of table --
SELECT name, score FROM second_table WHERE name!='' OR name IS NOT NULL ORDER BY score DESC;
