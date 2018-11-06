DROP procedure receiverhospitalshoworgan; 

DELIMITER $$

CREATE PROCEDURE receiverhospitalshoworgan(IN p_emailID VARCHAR(45))
BEGIN
	SELECT organ FROM user WHERE emailID=p_emailID AND donationType='r';
END $$

DELIMITER ;