from flask import url_for
from organdonationwebapp import ac
import base64

class Admin(object):
    def initialize(self,adminJson):
        self.emailID = adminJson['emailID'] if 'emailID' in adminJson else None
        passwrd = adminJson['password'] if 'password' in adminJson else None
        self.password = base64.b64encode(passwrd.encode())

    def register(self):
        return NotImplementedError

    def login(self):
        try:
            self.logger.info("admin logger initiliazed")
            if(ac.adminLoginAuthentication(self.emailID, self.password,self.logger)):
                url = ('/adminhome/'+ self.emailID)
                self.logger.debug("Admin " + self.emailID + " logged in Successfully.")
                return True, url
            else:
                self.logger.error("Authentication Failed. Please register if not a registered User")
                return False, "Authentication Failed. Please register if not a registered User"
        except Exception as err:
            self.logger.error(err)
            return err
 
    
    def setLogger(self,logger):
        self.logger = logger

def build_Admin(cls,adminJson, logger):
    admin = cls()
    admin.initialize(adminJson)
    admin.setLogger(logger)
    return admin