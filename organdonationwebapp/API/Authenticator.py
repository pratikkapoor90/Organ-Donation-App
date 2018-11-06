
import organdonationwebapp.API.UserTypeFactory as factory

class Authenticator(object):
    def __init__(self,loginJson, logger):
        self.usertype = loginJson['logintype'] if 'logintype' in loginJson else None
        self.email = loginJson['emailID'] if 'emailID' in loginJson else None
        self.password = loginJson['password'] if 'password' in loginJson else None
        self.json = loginJson
        self.logger = logger

    def validateLogin(self):
        try:
            objectFactory = factory.UserTypeFactory(self.json,self.logger ,None, self.usertype,)
            inst = objectFactory.createObject()
            valid, url = inst.login()
            return valid, url
        except Exception as err:
            print(err)
            return None