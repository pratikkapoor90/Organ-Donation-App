from flask import Flask, render_template, request, redirect, session, url_for, g, send_file,flash, jsonify
from organdonationwebapp import app, sc
import organdonationwebapp.User.User as us
import organdonationwebapp.User.OpenRequestDetails as rdo
import organdonationwebapp.Hospital.HospitalList as hlo
import organdonationwebapp.User.Donor.Donor as do
import organdonationwebapp.User.Recipient.Recipient as ro
import organdonationwebapp.User.Donor.UpdateRequestStatus as uro
import organdonationwebapp.API.Register as res
import organdonationwebapp.User.UpdateMedicalReports as umr
import organdonationwebapp.User.ViewUserReports as vur
import organdonationwebapp.API.Logger as log
import json
import binascii
from io import BytesIO
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadTimeSignature
app.config.from_pyfile('../config.cfg')

@app.before_request
def before_request():
    g.logger = log.MyLogger.__call__().get_logger()



mail = Mail(app)

@app.route('/signup/<usertype>', methods=['GET','POST'])
def registerUser(usertype = None):
    organ =[]
    hospitalList = hlo.HospitalList(g.logger)
    hospital_list = hospitalList.getGlobalHospitalList()
    if request.method == 'POST':
        user_dict = request.form.to_dict()
        organ = request.form.getlist('organ')
        user_dict['organ'] = organ
        user_data= json.dumps(user_dict)
        registerJson = json.loads(user_data)
        registerObject = res.Register(registerJson,g.logger, None, usertype)
        valid, url = registerObject.registerEntity()
        if(valid):
            if(g.user):
                flash ("Registered Successfully")
                return redirect(url_for('hospitalHome', emailID = g.user))
            else:
                flash ("Registered Successfully")
                return redirect(url_for('Login'))
        else:
            flash("Registration error")
            return "<h2> Registration failed </h2>"
    return render_template('signup.html', hlist=hospital_list)


@app.route('/donorhospitalrequest/<requestID>', methods=['GET','POST'])
def donorHospitalRequestPage(requestID=None):
    donor_userdata = None
    recipient_userdata = None
    requestdata =rdo.OpenRequestDetails(requestID,g.logger)
    request_userdata = requestdata.getOpenRequestData()
    donorEmail=request_userdata[0][0]
    recipientEmail=request_userdata[0][1]
    organ=request_userdata[0][2]
    requestState=request_userdata[0][3]
    if(donorEmail):
        donor = do.Donor(donorEmail,g.logger)
        donor_userdata = donor.donorHospitalRequestPage()
    if(recipientEmail):
        recipient = ro.Recipient(recipientEmail, g.logger)
        recipient_userdata = recipient.donorHospitalPageRecipientList()
    if(recipient_userdata and donor_userdata):
        if request.method == 'POST':
            request1= json.dumps(request.form.to_dict())
            request_json = json.loads(request1) 
            if('report' in request_json):
                Email = request_json['report'] if 'report' in request_json else None
                usertype = 'r'
                reports =vur.ViewUserReports(Email,usertype,g.logger)
                report = reports.viewReports()
                if(report):
                    return send_file(BytesIO(report[0][0]), attachment_filename='reports.pdf')
            if('upload' in request_json):
                if('reports' in request_json):
                    flash("please insert a valid certificates")
                else:
                    data = request.files['reports']
                    breport=data.read()
                    report =binascii.hexlify(breport)
                    userType= "d"
                    donorReport= umr.UpdateMedicalReports(donorEmail,userType, report,g.logger)
                    donor_report_status = donorReport.updateReports()
                    if(donor_report_status):
                        flash("Updated Successfully")
                    else:
                        flash("Insertion Error!")
            if('submit' in request_json):
                updateRequestStatus = uro.UpdateRequestStatus(request_json['submit'], requestID,recipientEmail, g.logger)
                request_status = updateRequestStatus.setRequestsStatus()
                send_email= updateRequestStatus.sendEmail()
                if(request_status and send_email):
                    flash("Request Status updated successfully")
                    return redirect(url_for('hospitalHome', emailID = g.user))
                else:
                    flash("Error updating request status. Please try again later!")
            if('email' in request_json):
                Email = request_json['email'] if 'email' in request_json else None
                msg = Message('Receiver Donor Request', sender= 'amcamcwinter@gmail.com', recipients=[Email])
                msg.body = 'A New Request has been generated for your organ. Please contact your Hospital  as soon as possible'
                mail.send(msg)
                flash("Email Sent Successfully")
        return render_template('DonorReceiverRequest.html', recipientdata=recipient_userdata, donordata=donor_userdata, organ=organ, requestState=requestState)
    else:
        flash("No donor/reciever available for this Request!")
        return render_template('DonorReceiverRequest.html', recipientdata=recipient_userdata, donordata=donor_userdata, organ=organ, requestState=requestState)