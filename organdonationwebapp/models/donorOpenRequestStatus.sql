DROP procedure donorOpenRequestStatus; 

DELIMITER $$

CREATE PROCEDURE donorOpenRequestStatus(IN p_hospitalID VARCHAR(45), p_donorID VARCHAR(45))
BEGIN
	SELECT * FROM requestdata WHERE hospitalID=p_hospitalID AND donorID=p_donorID;
END $$

DELIMITER ;