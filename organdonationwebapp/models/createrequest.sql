DROP procedure createrequest; 

DELIMITER $$

CREATE PROCEDURE createrequest(IN P_donorID VARCHAR(50),P_recipientID VARCHAR(50),P_organRequested VARCHAR(20),P_hospitalID VARCHAR(50),P_requestState INT(11))
BEGIN
	INSERT INTO requestdata(donorID,recipientID,organRequested,hospitalID,requestState) VALUES (P_donorID,P_recipientID,P_organRequested,P_hospitalID,P_requestState);
END $$

DELIMITER ;