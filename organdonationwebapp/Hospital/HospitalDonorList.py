from organdonationwebapp import hc

class HospitalDonorList(object):
    def __init__(self,hospitalName, logger):
        self.hospitalName = hospitalName
        self.logger = logger

    def getDonorList(self):
        try:
            donor_list = hc.getHospitalDonorList(self.hospitalName, self.logger)
            if(donor_list):
                return donor_list
        except Exception as err:
            return err