DROP procedure gethospitalcertificate; 

DELIMITER $$

CREATE PROCEDURE gethospitalcertificate(IN p_emailID VARCHAR(45))
BEGIN
	SELECT certificate FROM hospital WHERE emailID=p_emailID;
END $$

DELIMITER ;