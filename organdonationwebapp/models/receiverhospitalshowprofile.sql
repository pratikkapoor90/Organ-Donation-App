DROP procedure receiverhospitalshowprofile; 

DELIMITER $$

CREATE PROCEDURE receiverhospitalshowprofile(IN p_emailID VARCHAR(45))
BEGIN
	SELECT userFirstName, userLastName, emailID, dob, sex, hospital FROM user WHERE emailID=p_emailID AND donationType='r';
END $$

DELIMITER ;