DROP procedure gethospitalID; 

DELIMITER $$

CREATE PROCEDURE gethospitalID(IN P_hospitalName VARCHAR(100))
BEGIN
	SELECT  emailID FROM hospital where hospitalName=P_hospitalName;
END $$

DELIMITER ;