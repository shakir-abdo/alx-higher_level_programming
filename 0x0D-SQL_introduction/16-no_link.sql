-- lists all records of the table second_table of the database hbtn_0c_0 in MySQL server.
-- records are ordered by descending score.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
