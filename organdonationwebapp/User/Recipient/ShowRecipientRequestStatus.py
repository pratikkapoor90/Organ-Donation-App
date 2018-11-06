from organdonationwebapp import ruc


class ShowRecipientRequestStatus(object):
    def __init__(self,recipientEmail):
        self.recipientEmail = recipientEmail


    def getRequestsStatus(self):
        try:
            request_status_data = ruc.getOpenRequestsStatus(self.recipientEmail)
            request_data = {"approved": [], "rejected": [], "pending": []}
            if(request_status_data):
                for item in request_status_data:
                    if(item[5] == 1):
                        request_data["approved"].append(item)
                    elif(item[5] == 2):
                        request_data["rejected"].append(item)
                    elif(item[5] == 0 or item[5] == ""):
                        request_data["pending"].append(item)
            return request_data
        except Exception as err:
            return None