-- makes a stored procedure that adds an entry to the database
DELIMITER //

CREATE PROCEDURE AddBonus(user_id INT, project_name VARCHAR(255), score FLOAT)
BEGIN
	DECLARE project_id INT;
	-- get value of id and store it in the project_id variable
	SELECT id INTO project_id
	FROM projects
	WHERE name = project_name;
	-- check if value is NULL
	IF project_id IS NULL THEN
		INSERT INTO projects(name)
		VALUES(project_name);
		SELECT id INTO project_id
		FROM projects
		WHERE name = project_name;
	END IF;

	INSERT INTO corrections
	VALUES(user_id, project_id, score);

END
//


DELIMITER ;
