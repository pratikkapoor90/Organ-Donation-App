from organdonationwebapp import hc

class DonorHospitalID(object):
    def __init__(self,donorHospitalName):
        self.donorHospitalName = donorHospitalName
            

    def getDonorHospitalID(self):
        try:
            hospitalID = hc.getHospitalID(self.donorHospitalName)
            if(hospitalID):
                return hospitalID
            else:
                return None
        except Exception as err:
            return err