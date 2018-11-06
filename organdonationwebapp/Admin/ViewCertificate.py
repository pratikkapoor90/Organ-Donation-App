from organdonationwebapp import ac

class ViewCertificate(object):
    def __init__(self,email, logger):
        self.hospitalEmail = email
        self.logger = logger
            
    def getHospitalCerti(self):
        try:
            self.logger.info("getHospitalCerti logger initialized")
            Result = ac.getHospitalCertificate(self.hospitalEmail,self.logger)
            if(Result):
                return Result
            else:
                self.logger.info("getHospitalCerti returned none")
                return None
        except Exception as err:
            self.logger.error(err)
            return None