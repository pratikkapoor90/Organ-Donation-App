from organdonationwebapp import duc


class ShowDonorProfile(object):
    def __init__(self,donorEmail, logger):
        self.donorEmail = donorEmail
        self.logger = logger


    def getDonorProfile(self):
        try:
            self.logger.info("getDonorProfile logger initilaized")
            donor_data = duc.donorHospitalShowDonorProfile(self.donorEmail, self.logger)
            if(donor_data):
                return donor_data
            else:
                self.logger.debug("getDonorOrgans returned None")
                return None
        except Exception as err:
            self.logger.error(err)
            return err


    def getDonorOrgans(self):
        try:
            self.logger.info("getDonorOrgans logger initilaized")
            donor_organ_data = duc.showDonorOrgan(self.donorEmail,self.logger)
            if(donor_organ_data):
                return donor_organ_data
            else:
                self.logger.debug("getDonorOrgans returned None")
                return None
        except Exception as err:
            self.logger.error(err)
            return err