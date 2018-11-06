from flask import Flask, render_template, request, redirect, session, url_for, g, send_file,flash, jsonify
from organdonationwebapp import app
import organdonationwebapp.User.Donor.DonorListDetails as dlo
import organdonationwebapp.User.Donor.ShowDonorProfile as dop
import organdonationwebapp.Hospital.HospitalHome as hho
import organdonationwebapp.Hospital.HospitalDonorList as hdl
import organdonationwebapp.User.Donor.ShowDonorRequestStatus as rso
import organdonationwebapp.API.Logger as log
import json


@app.before_request
def before_request():
    g.logger = log.MyLogger.__call__().get_logger()

@app.route('/donorList', methods=['GET','POST'])
def donorList():
    print("g.user",(g.user))
    if g.user:
        hospitalEmail = g.user
        hospitalhome = hho.HospitalHome(hospitalEmail,g.logger)
        hospital_name = hospitalhome.getHospitalName()
        donorlist = dlo.DonorListDetails(hospital_name,g.logger)
        don_list_details = donorlist.getDonorsList(hospital_name,g.logger)
        if(don_list_details):
            if request.method == 'POST':
                data= json.dumps(request.form.to_dict())
                data_json = json.loads(data)
                if('view' in data_json):
                    donorEmail = request.form["view"]
                    return redirect(url_for('donorProfilePage', hospitalEmail=hospitalEmail, donorEmail=donorEmail))
            return render_template('donorList.html', dlist=don_list_details)
        return render_template('donorList.html')
    return redirect(url_for('Login'))


@app.route('/donorprofile/<hospitalEmail>/<donorEmail>', methods=['GET','POST'])
def donorProfilePage(hospitalEmail=None,donorEmail=None):
    donorprofile = dop.ShowDonorProfile(donorEmail,g.logger)
    donor_userdata = donorprofile.getDonorProfile()
    donor_organ_data = donorprofile.getDonorOrgans()
    requestStatus = rso.ShowDonorRequestStatus(hospitalEmail,donorEmail, g.logger)
    request_status_data = requestStatus.getRequestsStatus()
    approved_requests = request_status_data["approved"]
    pending_requests = request_status_data["pending"]
    if(donor_userdata and donor_organ_data):
        if request.method == 'POST':
            data= json.dumps(request.form.to_dict())
            datajson = json.loads(data)
            if('requestID' in datajson):
                requestID = request.form['requestID']
                return redirect(url_for('donorHospitalRequestPage', requestID=requestID))
        return render_template('donorprofile.html', hospitalEmail=hospitalEmail, donorEmail=donorEmail, pending_requests=pending_requests, approved_requests=approved_requests, donordata=donor_userdata, organ_data=donor_organ_data)