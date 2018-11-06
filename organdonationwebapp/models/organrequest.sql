DROP procedure organrequest; 

DELIMITER $$

CREATE PROCEDURE organrequest(IN P_requestID VARCHAR(45))
BEGIN
	SELECT donorID, recipientID, organRequested, requestState FROM requestdata WHERE requestID=P_requestID;
    
END $$

DELIMITER ;