from organdonationwebapp import ruc

class NewDonationRequest(object):
    def __init__(self, donorEmail, recipientEmail, donatingOrgan, donorHospital, logger):
        self.donorEmail = donorEmail
        self.recipientEmail = recipientEmail
        self.donatingOrgan = donatingOrgan
        self.donorHospital = donorHospital
        self.logger = logger

    def createDonationRequest(self):
        try:
            self.logger.info("createDonationRequest logger initilaized")
            if(ruc.createRequest(self.donorEmail, self.recipientEmail, self.donatingOrgan, self.donorHospital, self.logger)):
                return True
            else:
                self.logger.debug("createDonationRequest returns Flase")
                return False
        except Exception as err:
            self.logger.error(err)
            return err