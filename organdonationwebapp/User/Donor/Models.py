from organdonationwebapp.models.SqlClient import SqlClient

class DonorModel(SqlClient):
    def __init__(self):
        super(DonorModel,self).__init__()


    def donorHospitalShowDonorProfile(self, donorEmail, logger):
        self.logger = logger
        try:
            self.logger.info("donorHospitalShowDonorProfile logger initialized")
            SqlClient.startDBConnection(self)
            self.cursor.callproc('donorhospitalshowdonorprofile',[donorEmail])
            res = self.cursor.stored_results()
            for result in res:
                userdata= result.fetchall()
                if(userdata):
                    SqlClient.closeDBConnection(self)
                    self.logger.info("donorHospitalShowDonorProfile DBconn closed")
                    return userdata
                else:
                    self.logger.debug("donorHospitalShowDonorProfile returned None")
                    SqlClient.closeDBConnection(self)
                    self.logger.info("donorHospitalShowDonorProfile DBconn closed")
                    return None
        except Exception as err:
            self.logger.error(err)
            SqlClient.closeDBConnection(self)
            self.logger.info("donorHospitalShowDonorProfile DBconn closed")
            return err


    def showDonorOrgan(self, donorEmail, logger):
        self.logger = logger
        try:
            self.logger.info("showDonorOrgan logger initialized")
            SqlClient.startDBConnection(self)
            self.cursor.callproc('donorshoworgan',[donorEmail])
            res = self.cursor.stored_results()
            for result in res:
                userdata_organ= result.fetchall()
                for row in userdata_organ:
                    organ = row[0]
                if(userdata_organ):
                    SqlClient.closeDBConnection(self)
                    self.logger.info("showDonorOrgan DBconn closed")
                    return userdata_organ
                else:
                    self.logger.debug("showDonorOrgan returned None")
                    SqlClient.closeDBConnection(self)
                    self.logger.info("showDonorOrgan DBconn closed")
                    return None
        except Exception as err:
            self.logger.error(err)
            SqlClient.closeDBConnection(self)
            self.logger.info("donorHospitalShowDonorProfile DBconn closed")
            return err


    def recommendedDonorList(self, organ, logger):
        self.logger = logger
        try:
            SqlClient.startDBConnection(self)
            self.logger.info("recommendedDonorList logger initilized")
            self.cursor.callproc('recommendeddonorlist',[organ])
            res = self.cursor.stored_results()
            for result in res:
                organ_data= result.fetchall()
                if(organ_data):
                    SqlClient.closeDBConnection(self)
                    self.logger.debug("recommendedDonorList DBconn closed")
                    return organ_data
                else:
                    SqlClient.closeDBConnection(self)
                    self.logger.debug("recommendedDonorList DBconn closed")
                    return None
        except Exception as err:
            SqlClient.closeDBConnection(self)
            self.logger.debug("recommendedDonorList DBconn closed")
            self.logger.error(err)
            return None


    def getDonorList(self, hname, logger):
        self.logger = logger
        try:
            self.logger.info("getDonorList logger initialized")
            SqlClient.startDBConnection(self)
            self.cursor.callproc('gethospitaldonorlist',[hname])
            res = self.cursor.stored_results()
            for result in res:
                donorlist= result.fetchall()
                SqlClient.closeDBConnection(self)
                self.logger.debug("getDonorList DBconn closed")
                return donorlist
        except Exception as err:
            self.logger.error(err)
            SqlClient.closeDBConnection(self)
            self.logger.info("getDonorList DBconn closed")
            return err


    def setRequestsStatus(self, requestID, requeststate, logger):
        self.logger = logger
        try:
            self.logger.info("setRequestsStatus logger initialized")
            SqlClient.startDBConnection(self)
            self.cursor.callproc('updaterequeststate',[requestID,requeststate])
            self.connection.commit()
            SqlClient.closeDBConnection(self)
            self.logger.debug("setRequestsStatus DBconn closed")
            return True
        except Exception as err:
            self.logger.error(err)
            SqlClient.closeDBConnection(self)
            self.logger.debug("setRequestsStatus DBconn closed")
            return False


    def getOpenRequestsStatus(self, hospitalEmail, donorEmail, logger):
        self.logger = logger
        try:
            self.logger.info("getOpenRequestsStatus logger initialized")
            SqlClient.startDBConnection(self)
            self.cursor.callproc('donorOpenRequestStatus',[hospitalEmail,donorEmail])
            res = self.cursor.stored_results()
            for result in res:
                requeststatusdata= result.fetchall()
                if(requeststatusdata):
                    SqlClient.closeDBConnection(self)
                    self.logger.debug("getOpenRequestsStatus DBconn closed")
                    return requeststatusdata
                else:
                    SqlClient.closeDBConnection(self)
                    self.logger.debug("getOpenRequestsStatus DBconn closed")
                    return None
        except Exception as err:
            self.logger.error(err)
            SqlClient.closeDBConnection(self)
            self.logger.debug("getOpenRequestsStatus DBconn closed")
            return None