from organdonationwebapp import uc

class ViewUserReports(object):
    def __init__(self,emailID,UserType,logger):
        self.emailID = emailID
        self.userType = UserType
        self.logger = logger

    def viewReports(self):
        try:
            self.logger.info("viewReports logger initialized")
            result = uc.getReports(self.emailID, self.userType,self.logger)
            if(result):
                return result
            else:
                self.logger.debug("viewReports returned None")
                return None
        except Exception as err:
            self.logger.error(err)
            return err