from flask import url_for
from organdonationwebapp import uc

class User(object):
    def initialize(self,userJson):
        self.first_name = userJson['first_name'] if 'first_name' in userJson else None
        self.last_name = userJson['last_name'] if 'last_name' in userJson else None
        self.phone_number = userJson['phone_number'] if 'phone_number' in userJson else None
        self.email = userJson['email'] if 'email' in userJson else None
        self.sex = userJson['sex'] if 'sex' in userJson else None
        self.dob = userJson['dob'] if 'dob' in userJson else None
        self.address = userJson['address'] if 'address' in userJson else None
        self.province = userJson['province'] if 'province' in userJson else None
        self.city = userJson['city'] if 'city' in userJson else None
        self.hospital = userJson['hname'] if 'hname' in userJson else None
        self.bloodgroup = userJson['bloodgroup'] if 'bloodgroup' in userJson else None
        self.usertype = userJson['usertype'] if 'usertype' in userJson else None
        self.organ = userJson['organ'] if 'organ' in userJson else None


    def register(self):
        try:
            if(uc.userRegistration(self)):
                url = url_for('Login')
                self.logger.debug("User " + self.email + " registered Successfully.")
                return True, url
            else:
                self.logger.error("Registration failed for user" + self.email + "!!")
                return False, "Registration Failed."
        except Exception as err:
            self.logger.error(err)
            return err


    def setLogger(self,logger):
        self.logger = logger

    def login(self):
       return NotImplementedError

def build_User(cls,userJson, logger):
    user = cls()
    user.initialize(userJson)
    user.setLogger(logger)
    #validate certificate to add here
    return user