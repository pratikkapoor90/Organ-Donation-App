DROP procedure recommendeddonorlist; 

DELIMITER $$

CREATE PROCEDURE recommendeddonorlist(IN p_organ VARCHAR(45))
BEGIN
	SELECT emailID, organ, hospital, userFirstName, userLastName FROM user WHERE organ=p_organ AND donationType='d';
END $$

DELIMITER ;