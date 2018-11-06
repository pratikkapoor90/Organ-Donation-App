DROP procedure recipientOpenRequestStatus; 

DELIMITER $$

CREATE PROCEDURE recipientOpenRequestStatus(IN p_recipientID VARCHAR(45))
BEGIN
	SELECT * FROM requestdata WHERE recipientID=p_recipientID;
END $$

DELIMITER ;