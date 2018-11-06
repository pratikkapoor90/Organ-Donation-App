from organdonationwebapp import duc


class ShowDonorRequestStatus(object):
    def __init__(self,hospitalEmail,donorEmail, logger):
        self.hospitalEmail = hospitalEmail
        self.donorEmail = donorEmail
        self.logger = logger


    def getRequestsStatus(self):
        try:
            self.logger.info("getRequestsStatus logger initialized")
            request_status_data = duc.getOpenRequestsStatus(self.hospitalEmail,self.donorEmail, self.logger)
            request_data = {"approved": [], "pending": []}
            if(request_status_data):
                for item in request_status_data:
                    if(item[5] == 1):
                        request_data["approved"].append(item)
                    elif(item[5] == 0 or item[5] == ""):
                        request_data["pending"].append(item)
            return request_data
        except Exception as err:
            self.logger.error(err)
            return err