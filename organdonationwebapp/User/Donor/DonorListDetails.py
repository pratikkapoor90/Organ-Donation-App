from organdonationwebapp import duc

class DonorListDetails(object):
    def __init__(self,Email, logger):
        self.Email = Email
        self.logger = logger


    def getDonorsList(self, hname,logger):
        try:
            self.logger.info("getDonorsList logger initialized")
            self.hname = hname
            donor_list = duc.getDonorList(self.hname, logger)
            if(donor_list):
                return donor_list
            else:
                self.logger.debug("getDonorsList returned None")
                return None
        except Exception as err:
            self.logger.error(err)
            return err