DROP procedure updatereports; 

DELIMITER $$

CREATE PROCEDURE updatereports(IN P_emailID VARCHAR(100),P_type VARCHAR(100),P_reports LONGBLOB )
BEGIN
	update user set reports=UNHEX(P_reports) where emailID =P_emailID and donationType=P_type;
END $$

DELIMITER ;
