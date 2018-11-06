from organdonationwebapp import uc

class OpenRequestDetails(object):
    def __init__(self,requestID, logger):
        self.requestID = requestID
        self.logger = logger

    def getOpenRequestData(self):
        self.logger.info("getOpenRequestData logger initialized")
        try:
            request_userdata = uc.organRequest(self.requestID, self.logger)
            if(request_userdata):
                return request_userdata
            else:
                self.logger.debug("getOpenRequestData returned None")
                return None
        except Exception as err:
            self.logger.error(err)
            return err