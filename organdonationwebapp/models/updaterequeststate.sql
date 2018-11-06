DROP procedure updaterequeststate; 

DELIMITER $$

CREATE PROCEDURE updaterequeststate( IN P_requestID INT(11), P_requestState INT(11))
BEGIN
	UPDATE requestdata SET requestState= P_requestState WHERE requestID=P_requestID;
    
END $$

DELIMITER ;