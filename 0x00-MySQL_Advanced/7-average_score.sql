-- stored procedure creation for a procedure that finds the average score of a student
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
BEGIN
	DECLARE average_score FLOAT;
	SELECT AVG(score) INTO average_score
	FROM corrections
	WHERE corrections.user_id = user_id;
	-- update the record
	UPDATE users
	SET users.average_score = average_score
	WHERE id = user_id;
END
//

DELIMITER ;
