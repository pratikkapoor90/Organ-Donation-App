from flask import url_for
from organdonationwebapp import hc
import base64


class Hospital(object):
    def initialize(self,hospitalJson,certificateFile=None):
        self.hospitalName = hospitalJson['hospitalName'] if 'hospitalName' in hospitalJson else None
        self.emailID = hospitalJson['emailID'] if 'emailID' in hospitalJson else None
        self.phone = hospitalJson['phone'] if 'phone' in hospitalJson else None
        self.address = hospitalJson['address'] if 'address' in hospitalJson else None
        self.province = hospitalJson['province'] if 'province' in hospitalJson else None
        self.city = hospitalJson['city'] if 'city' in hospitalJson else None
        passwrd = hospitalJson['password'] if 'password' in hospitalJson else None
        self.password = base64.b64encode(passwrd.encode())
        self.data = certificateFile

    
    def register(self):
        try:
            self.logger.info("register logger initialized")
            if(hc.hospitalRegistration(self)):
                url = url_for('Login')
                self.logger.debug("Hospital " + self.emailID + " registered Successfully." )
                return True, url
            else:
                self.logger.error("Registration failed for hospital" + self.emailID + "!!")
                return False, "Registration Failed."
        except Exception as err:
            return err


    def setLogger(self,logger):
        self.logger = logger
            

    def login(self):
        try:
            self.logger.info("login logger initilized")
            result = hc.hospitalLoginAuthentication(self.emailID,self.password)
            if(result):
                url = ('/hospitalHome/' + self.emailID)
                self.logger.debug("Hospital " + self.emailID + " logged in Successfully." )
                return result, url
            else:
                self.logger.error("Hospital " + self.emailID + " log in failed." )
                return False, "Authentication Failed"  
        except Exception as err:
                    return err


#Adding factory for complex operation of initialization of hospital and validating certificate
def build_Hospital(cls,hospitalJson,logger,certificate = None):
    hosp = cls()
    hosp.initialize(hospitalJson,certificate)
    hosp.setLogger(logger)
    return hosp