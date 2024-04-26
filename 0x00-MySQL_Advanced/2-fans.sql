-- database gets the origin and count of fans as nb_fans from the database
SELECT origin, SUM(fans) AS nb_fans FROM metal_bands
	GROUP BY origin
	ORDER BY nb_fans DESC;
