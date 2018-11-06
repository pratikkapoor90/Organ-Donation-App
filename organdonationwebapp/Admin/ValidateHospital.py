from organdonationwebapp import ac

class ValidateHospital(object):
    def __init__(self,hospitalJson, logger):
        self.hospitalEmail = hospitalJson['validate'] if 'validate' in hospitalJson else None
        self.logger = logger
            
    def updateValidateHospitalFlag(self):
        try:
            self.logger.info("updateValidateHospitalFlag logger initialized")
            if(ac.validateHospital(self.hospitalEmail,self.logger)):
                return True
            else:
                self.logger.info("updateValidateHospitalFlag returned False")
                return False
        except Exception as err:
            self.logger.error(err)
            return err