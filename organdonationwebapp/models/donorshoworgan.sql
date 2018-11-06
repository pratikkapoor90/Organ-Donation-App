DROP procedure donorshoworgan; 

DELIMITER $$

CREATE PROCEDURE donorshoworgan(IN p_emailID VARCHAR(45))
BEGIN
	SELECT organ FROM user WHERE emailID=p_emailID AND donationType='d';
END $$

DELIMITER ;