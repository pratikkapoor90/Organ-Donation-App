from organdonationwebapp import hc

class HospitalRequestList(object):
    def __init__(self,emailID, logger):
        self.hospitalEmail = emailID
        self.logger = logger

    def getPendingRequestList(self):
        try:
            self.logger.info("getPendingRequestList logger initilized")
            request_list = hc.getHospitalRequestList(self.hospitalEmail, self.logger)
            if(request_list):
                return request_list
        except Exception as err:
            self.logger.error("getPendingRequestList",err)
            return err