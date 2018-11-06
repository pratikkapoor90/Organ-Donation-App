from organdonationwebapp.models.SqlClient import SqlClient


class HospitalModel(SqlClient):
    def __init__(self):
        super(HospitalModel,self).__init__()
    
    def hospitalRegistration(self,hospital):
        try:
            SqlClient.startDBConnection(self)
            self.cursor.callproc('hospitalregistration',[hospital.hospitalName,hospital.emailID,hospital.phone,hospital.address,hospital.province,hospital.city,hospital.password,hospital.data])
            self.connection.commit()
            SqlClient.closeDBConnection(self)
            return True
        except Exception as err:
            SqlClient.closeDBConnection(self)
            print(err)
            return False


    def hospitalLoginAuthentication(self,hemail,hpass):
        try:
            SqlClient.startDBConnection(self)
            print("hospitalLoginAuthentication")
            self.cursor.callproc('hospitallogin',[hemail,hpass])
            res = self.cursor.stored_results()
            for result in res:
                hospitalauth= result.fetchall()
                if(hospitalauth):
                    SqlClient.closeDBConnection(self)
                    print("hospitalLoginAuthentication Close")
                    return hospitalauth
                else:
                    SqlClient.closeDBConnection(self)
                    return None
        except Exception as err:
            print(err)
            SqlClient.closeDBConnection(self)
            return None        


    def getHospitalName(self,hemail,logger):
        self.logger = logger
        try:
            SqlClient.startDBConnection(self)
            self.logger.info(" getHospitalName logger intitlized")
            self.cursor.callproc('gethospitalname',[hemail])
            res = self.cursor.stored_results()
            for result in res:
                hname= result.fetchall()
                if(hname):
                    SqlClient.closeDBConnection(self)
                    self.logger.info(" getHospitalName DBconn closed")
                    return hname[0]
                else:
                    SqlClient.closeDBConnection(self)
                    self.logger.info(" getHospitalName DBconn closed")
                    return None
        except Exception as err:
            SqlClient.closeDBConnection(self)
            self.logger.error(err)
            return None


    def getHospitalList(self,logger):
        self.logger = logger
        try:
            SqlClient.startDBConnection(self)
            self.logger.info("getHospitalList logger initilized")
            self.cursor.callproc('hospitallist')
            res = self.cursor.stored_results()
            for result in res:
                hospitallist= result.fetchall()
                for row in hospitallist:
                    hospitalEmail = row[0]
                    validateFlag = row[1]
                if(hospitallist):
                    SqlClient.closeDBConnection(self)
                    self.logger.info("getHospitalList DBConn Closed")
                    return hospitallist
                else:
                    SqlClient.closeDBConnection(self)
                    self.logger.info("getHospitalList DBConn Closed")
                    return None
        except Exception as err:
            SqlClient.closeDBConnection(self)
            self.logger.error(err)
            return None


    def getHospitalID(self,donorHospitalName):
        try:
            SqlClient.startDBConnection(self)
            self.cursor.callproc('getHospitalID',[donorHospitalName])
            res = self.cursor.stored_results()
            for result in res:
                hospital_email= result.fetchone()
                if(hospital_email):
                    SqlClient.closeDBConnection(self)
                    return hospital_email
                else:
                    SqlClient.closeDBConnection(self)
                    return None
        except Exception as err:
            SqlClient.closeDBConnection(self)
            return None


    def getHospitalDonorList(self,hname, logger):
        self.logger = logger
        try:
            SqlClient.startDBConnection(self)
            self.logger.info("getHospitalDonorList logger initilized")
            self.cursor.callproc('gethospitaldonorlist',[hname])
            res = self.cursor.stored_results()
            for result in res:
                donorlist= result.fetchall()
                if(donorlist):
                    SqlClient.closeDBConnection(self)
                    return donorlist
                else:
                    SqlClient.closeDBConnection(self)
                    return None
        except Exception as err:
            self.logger.error(err)
            SqlClient.closeDBConnection(self)
            return None


    def getHospitalRecipientList(self,hname,logger):
        self.logger = logger
        try:
            SqlClient.startDBConnection(self)
            self.logger.info("getHospitalRecipientList logger initilized")
            self.cursor.callproc('gethospitalreceiverlist',[hname])
            res = self.cursor.stored_results()
            for result in res:
                receiverlist= result.fetchall()
                if(receiverlist):
                    SqlClient.closeDBConnection(self)
                    return receiverlist
                else:
                    SqlClient.closeDBConnection(self)
                    return None
        except Exception as err:
            self.logger.error(err)
            SqlClient.closeDBConnection(self)
            return None


    def getHospitalRequestList(self,emailID, logger):
        self.logger = logger
        try:
            SqlClient.startDBConnection(self)
            self.logger.info("getHospitalRequestList called for emailID" + emailID + "!!")
            self.cursor.callproc('requestlist', [emailID])
            res = self.cursor.stored_results()
            for result in res:
                requestlist= result.fetchall()
                if(requestlist):
                    self.logger.info("Values Fetched Successfully")
                    SqlClient.closeDBConnection(self)
                    return requestlist
                else:
                    SqlClient.closeDBConnection(self)
                    return None
        except Exception as err:
            self.logger.error(err)
            SqlClient.closeDBConnection(self)
            return None   


    def hospitalexist(self, hemail):
        SqlClient.startDBConnection(self)
        res = self.cursor.callproc('hospitalexist',[hemail,0])
        if(res[1]):
            SqlClient.closeDBConnection(self)
            return "Exist"
        else:
            SqlClient.closeDBConnection(self)
            return "NotExist"


    def getPassword(self):
        try:
            SqlClient.startDBConnection(self)
            self.cursor.callproc('validatePassword')
            res = self.cursor.stored_results()
            for result in res:
                passwordRules= result.fetchall()
                print(passwordRules)
                SqlClient.closeDBConnection(self)
                return passwordRules
        except Exception as err:
            SqlClient.closeDBConnection(self)
            return None