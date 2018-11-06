from flask import Flask, render_template, request, redirect, session, url_for, g, send_file,flash, jsonify
from organdonationwebapp import app
import organdonationwebapp.Admin.Admin as ao
import organdonationwebapp.Admin.ValidateHospital as vho
import organdonationwebapp.Admin.DeleteHospital as dho
import organdonationwebapp.Hospital.HospitalList as hlo
import organdonationwebapp.Admin.ViewCertificate as vc
import organdonationwebapp.API.Logger as log
import json
from io import BytesIO

@app.before_request
def before_request():
    g.logger = log.MyLogger.__call__().get_logger()

@app.route('/adminhome/<username>', methods=['GET','POST'])
def adminHomepage(username=None, hospitalEmail=None):
    hospitalList = hlo.HospitalList(g.logger)
    hospital_list = hospitalList.getGlobalHospitalList()
    if(hospital_list):
        if request.method == 'POST':
            validate_hospital = json.dumps(request.form.to_dict())
            hospital_json = json.loads(validate_hospital)
            if('validate' in hospital_json):
                validate = vho.ValidateHospital(hospital_json, g.logger)
                hospitalEmail = validate.updateValidateHospitalFlag()
                if(hospitalEmail):
                    return render_template('adminhome.html', username=username, list=hospital_list)
            if('delete' in hospital_json):
                hospitalID = hospital_json['delete']
                deleteHospital = dho.DeleteHospital(hospitalID,g.logger)
                delete_hospital_status = deleteHospital.deleteHospital()
                if(delete_hospital_status):
                    flash("deleted successfully")
                    return render_template('adminhome.html', list=hospital_list,username=username)
            if('certificate' in hospital_json):
                hospitalEmail = hospital_json['certificate'] if 'certificate' in hospital_json else None
                certificate = vc.ViewCertificate(hospitalEmail,g.logger)
                hospitalcertificate = certificate.getHospitalCerti()
                if(hospitalcertificate):
                    return send_file(BytesIO(hospitalcertificate[0][0]), attachment_filename='certificate.pdf')
        return render_template('adminhome.html', list=hospital_list,username=username)
    return render_template('adminhome.html', username=username)