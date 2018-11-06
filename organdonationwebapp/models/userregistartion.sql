DROP procedure userregistration; 

DELIMITER $$

CREATE PROCEDURE userregistration(IN P_firstName VARCHAR(50),P_lastName VARCHAR(50),P_phone VARCHAR(50),P_emailID VARCHAR(100) ,P_sex VARCHAR(50),P_dob VARCHAR(50),P_address VARCHAR(200),P_province VARCHAR(50),P_city VARCHAR(50),P_hospitalName VARCHAR(50),P_blood VARCHAR(50),P_donationtype VARCHAR(50),p_requestdate VARCHAR(20) ,P_organ VARCHAR(50) )
BEGIN
	INSERT INTO user(userFirstName,userLastName,phone,emailID,sex,dob,address,province,city,hospital,bloodGroup,donationType,requestdate,organ) VALUES (P_firstName,P_lastName,P_phone,P_emailID,P_sex,P_dob,P_address,P_province,P_city,P_hospitalName,P_blood,P_donationtype,p_requestdate,P_organ);
END $$

DELIMITER ;
