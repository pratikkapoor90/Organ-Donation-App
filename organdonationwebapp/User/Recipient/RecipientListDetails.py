from organdonationwebapp import ruc
class RecipientListDetails(object):
    def __init__(self,recipientEmail,logger):
        self.recipientEmail = recipientEmail
        self.logger = logger

    def getRecipientsList(self, hname, logger):
        try:
            self.logger.info("RecipientListDetails logger initialized")
            self.hname = hname
            recipient_list = ruc.getRecepientList(self.hname, logger)
            if(recipient_list):
                return recipient_list
            else:
                self.logger.debug("RecipientListDetails returns None")
                return None
        except Exception as err:
            self.logger.error(err)
            return err