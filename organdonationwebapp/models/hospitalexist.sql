DROP procedure hospitalexist;

DELIMITER $$

CREATE PROCEDURE hospitalexist(IN p_email VARCHAR(50), OUT P_out VARCHAR(50))
BEGIN
	SELECT emailID INTO p_out FROM hospital WHERE emailID= p_email;
END $$

DELIMITER ;
