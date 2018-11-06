class fakeViewCertificate(object):
    def __init__(self, emailid, certificate):
        self.emailid = emailid
        self.certificate = certificate
    def getHospitalCerti(self):
        return self.certificate

class fakeDeleteHospital(object):
    def __init__(self, emailid, isdeleted):
        self.emailid = emailid
        self.isdeleted = isdeleted
    def deleteHospital(self):
        return self.isdeleted

class fakeValidateHospital(object):
    def __init__(self, body,logger, isvalidated):
        self.body = body
        self.logger = logger
        self.isvalidated = isvalidated
    def updateValidateHospitalFlag(self):
        return self.isvalidated

class fakeHospitalList(object):
    def __init__(self, body):
        self.body = body
    def getGlobalHospitalList(self):
        return self.body

class fakeRegister(object):
    def __init__(self, regjson, utype, registered):
        self.regjson = regjson
        self.type = utype
        self.registered = registered
    def registerEntity(self):
        return self.registered, "url"

class fakeOpenRequestDetails(object):
    def __init__(self, requestid, body):
        self.requestid = requestid
        self.body = body
    def getOpenRequestData(self):
        return self.body

class fakeDonor(object):
    def __init__(self, donoremail, body):
        self.donoremail = donoremail
        self.body = body
    def donorHospitalRequestPage(self):
        return self.body

class fakeRecipient(object):
    def __init__(self, recipientemail, body):
        self.recipientemail = recipientemail
        self.body = body
    def donorHospitalPageRecipientList(self):
        return self.body

class fakeViewUserReports(object):
    def __init__(self, email, usertype, body):
        self.email = email
        self.usertype = usertype
        self.body = body
    def viewReports(self):
        return self.body

class fakeUpdateMedicalReports(object):
    def __init__(self, emailid, reports, usertype, isupdated):
        self.emailid = emailid
        self.reports = reports
        self.usertype = usertype
        self.isupdated = isupdated
    def updateReports(self):
        return self.isupdated

class fakeUpdateRequestStatus(object):
    def __init__(self, request, 
                 requestid, emailid, body, 
                 reqstatus, emailsent):
        self.requestid = requestid
        self.request = request
        self.emailid = emailid
        self.body = body
        self.reqstatus = reqstatus
        self.emailsent = emailsent
    def setRequestsStatus(self):
        return self.reqstatus
    def sendEmail(self):
        return self.emailsent                    

class mock_request_form(object):
    def __init__(self, body):
        self.body = body
    def to_dict(self):
        return self.body
    def getlist(self, organ):
        return self.body['organ']