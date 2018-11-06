DROP procedure donorhospitalshowdonorprofile; 

DELIMITER $$

CREATE PROCEDURE donorhospitalshowdonorprofile(IN p_emailID VARCHAR(45))
BEGIN
	SELECT * FROM user WHERE emailID=p_emailID AND donationType='d';
END $$

DELIMITER ;