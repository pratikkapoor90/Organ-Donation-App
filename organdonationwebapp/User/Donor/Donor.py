from organdonationwebapp import duc


class Donor(object):
    def __init__(self,donorEmail, logger):
        self.donorEmail = donorEmail
        self.logger = logger

    def donorHospitalRequestPage(self):
        try:
            self.logger.info("donorHospitalRequestPage logger initialized")
            donor_data = duc.donorHospitalShowDonorProfile(self.donorEmail, self.logger)
            if(donor_data):
                return donor_data
            else:
                self.logger.debug("donorHospitalRequestPage returned none")
                return None
        except Exception as err:
            self.logger.error(err)
            return err