from organdonationwebapp import duc

class ShowRecommendedDonors(object):
    def __init__(self,donororgan,logger):
        self.donororgan = donororgan
        self.logger = logger

    def getrecommendedDonorList(self):
        try:
            self.logger.info("getrecommendedDonorList logger initialized")
            matching_donors = duc.recommendedDonorList(self.donororgan, self.logger)
            if(matching_donors):
                return matching_donors
            else:
                self.logger.debug("getrecommendedDonorList returned None")
                return None
        except Exception as err:
            self.logger.error(err)
            return err