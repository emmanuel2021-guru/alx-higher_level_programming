-- lists the number of records with the same score in the table 'second_table' of the database 'hbtn_0c' in MySQL server
SELECT score, COUNT(score) as 'number' FROM second_table GROUP BY score ORDER BY COUNT(score) DESC;
