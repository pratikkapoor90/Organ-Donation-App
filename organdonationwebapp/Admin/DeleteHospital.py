from organdonationwebapp import ac

class DeleteHospital(object):
    def __init__(self,emailID, logger):
        self.hospitalEmail = emailID
        self.logger = logger
            
    def deleteHospital(self):
        try:
            self.logger.info("deleteHospital logger initialized")
            if(ac.deleteHospital(self.hospitalEmail, self.logger)):
                self.logger.info("Hospital " + self.hospitalEmail + " deleted Successfully." )
                return True
            else:
                self.logger.error("error deleting Hospital")
                return False
        except Exception as err:
            self.logger.error(err)
            return err