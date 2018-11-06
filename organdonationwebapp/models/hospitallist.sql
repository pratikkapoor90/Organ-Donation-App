DROP procedure hospitallist; 

DELIMITER $$

CREATE PROCEDURE hospitallist()
BEGIN
	SELECT * FROM hospital;
END $$

DELIMITER ;
