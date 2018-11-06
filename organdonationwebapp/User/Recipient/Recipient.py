from organdonationwebapp import ruc


class Recipient(object):
    def __init__(self,recipientEmail,logger):
        self.recipientEmail = recipientEmail
        self.logger = logger

    def donorHospitalPageRecipientList(self):
        try:
            self.logger.info("donorHospitalPageRecipientList logger initialized")
            recipient_data = ruc.donorHospitalShowReceiverProfile(self.recipientEmail,self.logger)
            if(recipient_data):
                return recipient_data
            else:
                self.logger.debug("donorHospitalPageRecipientList Returned None")
                return None
        except Exception as err:
            self.logger.error(err)
            return err