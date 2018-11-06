DROP procedure deletehospital; 

DELIMITER $$

CREATE PROCEDURE deletehospital(IN P_emailID VARCHAR(100))
BEGIN
	DELETE FROM hospital WHERE emailID =P_emailID;
END $$

DELIMITER ;