from organdonationwebapp import hc

class HospitalList(object):
    def __init__(self,logger):
        self.logger = logger

    def getGlobalHospitalList(self):
        try:
            self.logger.info("getGlobalHospitalList logger initilized")
            hospital_list = hc.getHospitalList(self.logger)
            if(hospital_list):
                return hospital_list
            else:
                self.logger.debug("getGlobalHospitalList returned None values")
                return None
        except Exception as err:
            self.logger.error("getGlobalHospitalList",err)
            return err
