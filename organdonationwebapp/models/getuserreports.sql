DROP procedure getuserreports; 

DELIMITER $$

CREATE PROCEDURE getuserreports(IN p_emailID VARCHAR(45), p_donationType VARCHAR(45))
BEGIN
	SELECT reports FROM user WHERE emailID=p_emailID and donationType = p_donationType;
END $$

DELIMITER ;