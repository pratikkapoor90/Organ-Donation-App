from organdonationwebapp import hc

class HospitalRecipientList(object):
    def __init__(self,hospitalName,logger):
        self.hospitalName = hospitalName
        self.logger = logger

    def getRecipientList(self):
        try:
            self.logger.info("getRecipientList logger initilized")
            recipient_list = hc.getHospitalRecipientList(self.hospitalName, self.logger)
            if(recipient_list):
                return recipient_list
        except Exception as err:
            self.logger.error("getRecipientList",err)
            return err