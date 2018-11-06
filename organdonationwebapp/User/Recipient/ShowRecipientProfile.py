from organdonationwebapp import ruc

class ShowRecipientProfile(object):
    def __init__(self,recipientEmail, logger):
        self.recipientEmail = recipientEmail
        self.logger = logger

    def getRecipientProfile(self):
        try:
            self.logger.info("getRecipientProfile logger initilaized")
            recipient_data = ruc.receiverHospitalShowProfile(self.recipientEmail, self.logger)
            if(recipient_data):
                return recipient_data
            else:
                self.logger.debug("getRecipientProfile returns None")
                return None
        except Exception as err:
            self.logger.error(err)
            return err

    def getRecipientOrgans(self):
        try:
            self.logger.info("getRecipientOrgans logger initilaized")
            recipient_organ_data = ruc.receiverHospitalShowOrgan(self.recipientEmail, self.logger)
            if(recipient_organ_data):
                return recipient_organ_data
            else:
                self.logger.debug("getRecipientOrgans returns None")
                return None
        except Exception as err:
            self.logger.error(err)
            return err