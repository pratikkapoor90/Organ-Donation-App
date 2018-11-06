from flask import Flask, render_template, request, redirect, session, url_for, g, send_file,flash, jsonify
from organdonationwebapp import app
import organdonationwebapp.User.Recipient.RecipientListDetails as rlo
import organdonationwebapp.User.Recipient.ShowRecipientProfile as rpo
import organdonationwebapp.User.Donor.ShowRecommendedDonors as dpo
import organdonationwebapp.User.Recipient.ShowRecipientRequestStatus as sro
import organdonationwebapp.User.UpdateMedicalReports as rro
import organdonationwebapp.Hospital.HospitalHome as hho
import organdonationwebapp.Hospital.DonorHospitalID as dho
import organdonationwebapp.User.Recipient.NewDonationRequest as dro
import organdonationwebapp.User.OpenRequestDetails as rdo
import organdonationwebapp.User.Donor.Donor as do
import organdonationwebapp.User.Recipient.Recipient as ro
import organdonationwebapp.User.Donor.UpdateRequestStatus as uro
import organdonationwebapp.User.ViewUserReports as vur
import organdonationwebapp.API.Logger as log
import json
import binascii
from io import BytesIO

@app.before_request
def before_request():
    g.logger = log.MyLogger.__call__().get_logger()


@app.route('/receiverList', methods=['GET', 'POST'])
def receiverList():
    if g.user:
        hospitalhome = hho.HospitalHome(g.user,g.logger)
        hospital_name = hospitalhome.getHospitalName()
        recipientlist = rlo.RecipientListDetails(hospital_name,g.logger)
        rec_list_details = recipientlist.getRecipientsList(hospital_name,g.logger)
        if(rec_list_details):
            if request.method == 'POST':
                recipientEmail = request.form['view']
                return redirect(url_for('receiverHospitalRequestPage',recipientEmail=recipientEmail))
            return render_template('receiverList.html', rlist=rec_list_details)
        return render_template('receiverList.html')
    return redirect(url_for('Login'))


@app.route('/receiverhospitalrequest/<recipientEmail>', methods=['GET','POST'])
def receiverHospitalRequestPage(recipientEmail=None):
    recipient_data = rpo.ShowRecipientProfile(recipientEmail,g.logger)
    recipient_profile = recipient_data.getRecipientProfile()
    print(recipient_profile)
    recipientEmail = recipient_profile[0][2] # Extracting recipient email from Recipient profile JSON
    recipient_organ_data = recipient_data.getRecipientOrgans()
    donor_organ_list = []
    only_organ_list = []
    for organ in recipient_organ_data:
        donor_list = dpo.ShowRecommendedDonors(organ[0], g.logger)
        donor_organ_list.extend(donor_list.getrecommendedDonorList())
    requestStatus = sro.ShowRecipientRequestStatus(recipientEmail)
    request_status_data = requestStatus.getRequestsStatus()
    approved_requests = request_status_data["approved"]
    rejected_requests = request_status_data["rejected"]
    pending_requests = request_status_data["pending"]
    if(recipient_profile and recipient_organ_data):
        if request.method == 'POST':
            donor_data= json.dumps(request.form.to_dict())
            donor_json = json.loads(donor_data)
            if('upload' in donor_json):
                if('reports' in donor_json):
                    flash("Please insert a valid certificates")
                else:
                    data = request.files['reports']
                    breport=data.read()
                    report =binascii.hexlify(breport)
                    userType= "r"
                    recipientReport= rro.UpdateMedicalReports(recipientEmail,userType,report, g.logger)
                    recipient_report_status = recipientReport.updateReports()
                    if(recipient_report_status):
                        flash("Updated Successfully")
                    else:
                        flash("Insertion Error!")
            if('create request' in donor_json):
                donor_json_values = donor_json['create request']
                donor_values_split = donor_json_values.split('_')
                donorEmail = donor_values_split[0]
                donatingOrgan = donor_values_split[1]
                donorHospitalName = donor_values_split[2]
                hospitalID = dho.DonorHospitalID(donorHospitalName)
                donorHospital = hospitalID.getDonorHospitalID()
                newRequest = dro.NewDonationRequest(donorEmail, recipientEmail, donatingOrgan, donorHospital[0],g.logger)
                if (newRequest.createDonationRequest()):
                    print("Request data inserted successfully")
                    flash ("Request Sent Successfully!!")
                    return render_template('receiverProfile.html', recipient_data=recipient_profile, organ_data=recipient_organ_data, donor_organ_data=donor_organ_list, pending_requests=pending_requests, approved_requests=approved_requests, rejected_requests=rejected_requests)
                else:
                    print("Error creating request")
                    flash ("Error Sending Request!!")
            if('view request' in donor_json):
                requestID = request.form['view request']
                return redirect(url_for('recipientShowApprovedRequest', requestID=requestID))
        return render_template('receiverProfile.html', recipient_data=recipient_profile, organ_data=recipient_organ_data, donor_organ_data=donor_organ_list, pending_requests=pending_requests, approved_requests=approved_requests, rejected_requests=rejected_requests)


@app.route('/recipientapprovedrequest/<requestID>', methods=['GET','POST'])
def recipientShowApprovedRequest(requestID=None):
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
        recipient = ro.Recipient(recipientEmail,g.logger)
        recipient_userdata = recipient.donorHospitalPageRecipientList()
    if(recipient_userdata and donor_userdata):
        if request.method == 'POST':
            request_data= json.dumps(request.form.to_dict())
            request_json = json.loads(request_data)
            if('submit' in request_json):
                updateRequestStatus = uro.UpdateRequestStatus(request.form['submit'], requestID, donorEmail,g.logger)
                request_status = updateRequestStatus.setRequestsStatus()
                send_email= updateRequestStatus.sendEmail()
                if(request_status and send_email):
                    flash("Request Status updated successfully")
                    return redirect(url_for('receiverHospitalRequestPage',recipientEmail=recipientEmail))
                else:
                    flash("Error updating request status. Please try again later!")
            
            if('dreport' in request_json):
                Email = request_json['dreport'] if 'dreport' in request_json else None
                usertype = 'd'
                reports =vur.ViewUserReports(Email,usertype,g.logger)
                report = reports.viewReports()
                if(report):
                    return send_file(BytesIO(report[0][0]), attachment_filename='reports.pdf')
                    
            if('rreport' in request_json):
                Email = request_json['rreport'] if 'rreport' in request_json else None
                usertype = 'r'
                reports =vur.ViewUserReports(Email,usertype,g.logger)
                report = reports.viewReports()
                if(report):
                    return send_file(BytesIO(report[0][0]), attachment_filename='reports.pdf')
        return render_template('RecipientShowRequestStatus.html', recipientdata=recipient_userdata, donordata=donor_userdata, organ=organ, requestState=requestState)
    else:
        flash("No donor/reciever available for this Request!")
        return render_template('RecipientShowRequestStatus.html', recipientdata=recipient_userdata, donordata=donor_userdata, organ=organ)