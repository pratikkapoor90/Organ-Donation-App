DROP procedure hospitalregistration; 

DELIMITER $$

CREATE PROCEDURE hospitalregistration(IN P_hospitalName VARCHAR(50),P_emailID VARCHAR(100),P_phone VARCHAR(50),P_address VARCHAR(200),P_province VARCHAR(50),P_city VARCHAR(50),P_password VARCHAR(100),P_certificate LONGBLOB )
BEGIN
	INSERT INTO hospital(hospitalName,emailID,phone,address,province,city,password,certificate) VALUES (P_hospitalName,P_emailID,P_phone,P_address,P_province,P_city,P_password,UNHEX(P_certificate));
END $$

DELIMITER ;
