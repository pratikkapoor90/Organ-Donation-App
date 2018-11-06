from organdonationwebapp import duc
from organdonationwebapp import app

from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadTimeSignature

app.config.from_pyfile('../config.cfg')

mail = Mail(app)

class UpdateRequestStatus(object):
    def __init__(self,request, requestID, userEmail,logger):
        self.request = request
        self.requestID = requestID
        self.userEmail = userEmail
        self.logger = logger


    def setRequestsStatus(self):
        try:
            self.logger.info("setRequestsStatus logger initialized")
            requeststate = 0        # 0 for any new pending requests
            if(self.request == "AcceptDonor"):
                self.logger.info("Donor Accepted Request")
                requeststate = 1    # 1 for requests accepted by Donors but pending at recipient's end for approval
            elif(self.request == "DeclineDonor"):
                self.logger.info("Donor Denied Request")
                requeststate = 2    # 2 for requests rejected by Donors
            elif(self.request == "AcceptRecipient"):
                self.logger.info("Receiver Accepted Request")
                requeststate = 3    # 3 for requests accepted by both Donor and Recipient
            elif(self.request == "DeclineRecipient"):
                self.logger.info("Receiver Denied Request")
                requeststate = 4    # 4 for requests rejected by Donors
            if(duc.setRequestsStatus(self.requestID, requeststate, self.logger)):
                return True
            else:
                self.logger.debug("setRequestsStatus returned None")
                return False
        except Exception as err:
            self.logger.error(err)
            return False


    def sendEmail(self):
        try:
            if(self.request == "AcceptDonor"):
                msg = Message('Receiver Intimitatiion', sender= 'amcamcwinter@gmail.com', recipients=[self.userEmail])
                msg.body = 'Your request has been accepted by the Donor'
                mail.send(msg)
                self.logger.info("Donor Accepted Request mail sent")
                return True
            elif(self.request == "DeclineDonor"):
                msg = Message('Receiver Intimitatiion', sender= 'amcamcwinter@gmail.com', recipients=[self.userEmail])
                msg.body = 'Your request has been denied by the Donor'
                mail.send(msg)
                self.logger.info("Donor Denied Request mail sent")
                return True
            elif(self.request == "AcceptRecipient"):
                msg = Message('Donor Intimitatiion', sender= 'amcamcwinter@gmail.com', recipients=[self.userEmail])
                msg.body = 'Your request has been accepted by the Receiver'
                mail.send(msg)
                self.logger.info("Receiver Accepted Request mail sent")
                return True
            elif(self.request == "DeclineRecipient"):
                msg = Message('Donor Intimitatiion', sender= 'amcamcwinter@gmail.com', recipients=[self.userEmail])
                msg.body = 'Your request has been denied by the Receiver'
                mail.send(msg)
                self.logger.info("Receiver Denied Request mail sent")
                return True
        except Exception as err:
            self.logger.error(err)
            return err
