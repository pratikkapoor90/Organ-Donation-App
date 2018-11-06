import organdonationwebapp.Hospital.Hospital as ho
import organdonationwebapp.Admin.Admin as ao
import organdonationwebapp.User.User as us

class UserTypeFactory(object):
    def __init__(self,Json,logger, certificate= None, usertype= None):
        self.certificate = certificate
        self.usertype = usertype
        self.json = Json
        self.logger = logger

    def createObject(self):
        try:
            self.logger.info("createObject logger initialized")
            if(self.usertype == "Hospital"):
                return ho.build_Hospital(ho.Hospital, self.json,self.logger, self.certificate)
            elif(self.usertype == "Donor or Receiver"):
                return us.build_User(us.User,self.json, self.logger)
            elif(self.usertype == "Admin"):
                return ao.build_Admin(ao.Admin,self.json, self.logger)
            else:
                return None
        except Exception as err:
            self.logger.error(err)
            return err