from organdonationwebapp import uc

class UpdateMedicalReports(object):
    def __init__(self,emailID,UserType,reports,logger):
        self.emailID = emailID
        self.reports = reports
        self.userType = UserType
        self.logger = logger

    def updateReports(self):
        try:
            self.logger.info("updateReports logger initialized")
            if(uc.updateReport(self.emailID, self.userType, self.reports, self.logger)):
                return True
            else:
                self.logger.debug("updateReports returned false")
                return False
        except Exception as err:
            self.logger.error(err)
            return err