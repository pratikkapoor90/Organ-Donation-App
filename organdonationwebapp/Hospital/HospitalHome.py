from organdonationwebapp import hc

class HospitalHome(object):
    def __init__(self,emailID,logger):
        self.hospitalEmail = emailID
        self.logger = logger
            

    def getHospitalName(self):
        try:
            self.logger.info("getHospitalName logger initilized")
            hospital_name = hc.getHospitalName(self.hospitalEmail, self.logger)
            if(hospital_name):
                return (hospital_name[0])
            else:
                self.logger.info(" getHospitalName returned None value")
                return None
        except Exception as err:
            self.logger.error(err)
            return err