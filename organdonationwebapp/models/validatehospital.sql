DROP procedure validatehospital; 

DELIMITER $$

CREATE PROCEDURE validatehospital( IN P_email VARCHAR(45))
BEGIN
	UPDATE hospital SET validate=true WHERE emailID=P_email;
    
END $$

DELIMITER ;