import mock
import organdonationwebapp.API.DonorRecipientViews as drview
from test_helpers import fakeViewCertificate, fakeHospitalList, fakeDeleteHospital, fakeValidateHospital, mock_request_form, fakeRegister, fakeOpenRequestDetails,\
                         fakeDonor, fakeRecipient, fakeViewUserReports, fakeUpdateMedicalReports, fakeUpdateRequestStatus


@mock.patch.object(drview, 'g')
def test_beforerequest(mock_g):
    drview.before_request()

@mock.patch.object(drview.hlo, 'HospitalList')
@mock.patch.object(drview.res, 'Register')
@mock.patch.object(drview, 'flash')
@mock.patch.object(drview, 'redirect')
@mock.patch.object(drview, 'url_for')
@mock.patch.object(drview, 'g')
@mock.patch.object(drview, 'request')
def test_registerUser(mock_request, mock_g, mock_url_for,
                      mock_redirect, mock_flash, mock_reg, mock_hlo_li):
    mock_hlo_li.return_value = fakeHospitalList("{\"hospitals\": \"[('hospital1', 'hospital1@test.com', 'address hospital1'), ('hospital2', 'hospital2@test.com', 'address hospital2')]")
    drview.request.method = 'POST'
    mock_g.user = "user"
    drview.request.form = mock_request_form({"username": "name", "address": "halifax", "type": "donor", "organ": ["liver", "heart"]})
    mock_reg.return_value = fakeRegister({"username": "name", "address": "halifax", "type": "donor", "organ": ["liver", "heart"]}, "donor", True)
    mock_flash.return_value = "Registered Successfully"
    mock_url_for.return_value = "http://url"
    mock_redirect.return_value = "<h2>hospital home</h2"
    assert drview.registerUser("donor") == "<h2>hospital home</h2"

@mock.patch.object(drview.hlo, 'HospitalList')
@mock.patch.object(drview, 'render_template')
@mock.patch.object(drview, 'g')
@mock.patch.object(drview, 'request')
def test_registerUser_get(mock_request, mock_g, mock_ren, mock_hlo_li):
    mock_hlo_li.return_value = fakeHospitalList("{\"hospitals\": \"[('hospital1', 'hospital1@test.com', 'address hospital1'), ('hospital2', 'hospital2@test.com', 'address hospital2')]")
    drview.request.method = 'GET'
    mock_ren.return_value = "<h2>sign up</h2"
    assert drview.registerUser("donor") == "<h2>sign up</h2"

@mock.patch.object(drview.hlo, 'HospitalList')
@mock.patch.object(drview.res, 'Register')
@mock.patch.object(drview, 'flash')
@mock.patch.object(drview, 'redirect')
@mock.patch.object(drview, 'url_for')
@mock.patch.object(drview, 'g')
@mock.patch.object(drview, 'request')
def test_registerUser_noguser(mock_request, mock_g, mock_url_for,
                      mock_redirect, mock_flash, mock_reg, mock_hlo_li):
    mock_hlo_li.return_value = fakeHospitalList("{\"hospitals\": \"[('hospital1', 'hospital1@test.com', 'address hospital1'), ('hospital2', 'hospital2@test.com', 'address hospital2')]")
    drview.request.method = 'POST'
    mock_g.user = None
    drview.request.form = mock_request_form({"username": "name", "address": "halifax", "type": "donor", "organ": ["liver", "heart"]})
    mock_reg.return_value = fakeRegister({"username": "name", "address": "halifax", "type": "donor", "organ": ["liver", "heart"]}, "donor", True)
    mock_flash.return_value = "Registered Successfully"
    mock_url_for.return_value = "http://url"
    mock_redirect.return_value = "<h2>login</h2"
    assert drview.registerUser("donor") == "<h2>login</h2"

@mock.patch.object(drview.hlo, 'HospitalList')
@mock.patch.object(drview.res, 'Register')
@mock.patch.object(drview, 'flash')
@mock.patch.object(drview, 'request')
@mock.patch.object(drview, 'g')
def test_registerUser_invalid(mock_g, mock_request, mock_flash, mock_reg, mock_hlo_li):
    mock_hlo_li.return_value = fakeHospitalList("{\"hospitals\": \"[('hospital1', 'hospital1@test.com', 'address hospital1'), ('hospital2', 'hospital2@test.com', 'address hospital2')]")
    drview.request.method = 'POST'
    drview.request.form = mock_request_form({"username": "name", "address": "halifax", "type": "donor", "organ": ["liver", "heart"]})
    mock_reg.return_value = fakeRegister({"username": "name", "address": "halifax", "type": "donor", "organ": ["liver", "heart"]}, "donor", False)
    mock_flash.return_value = "Registration error"
    assert drview.registerUser("donor") == "<h2> Registration failed </h2>"

@mock.patch.object(drview, 'send_file')
@mock.patch.object(drview, 'BytesIO')
@mock.patch.object(drview.vur, 'ViewUserReports')
@mock.patch.object(drview, 'request')
@mock.patch.object(drview, 'g')
@mock.patch.object(drview.ro, 'Recipient')
@mock.patch.object(drview.do, 'Donor')
@mock.patch.object(drview.rdo, 'OpenRequestDetails')
def test_donorHospitalRequestPage_report(mock_ord, mock_donor, mock_recipient, mock_g,
                                         mock_request, mock_vur, mock_bytesio, mock_send_file):
    mock_ord.return_value = fakeOpenRequestDetails("requestid", [("donor@test.com", "recipient@test.com", "organ", "pending")])
    mock_donor.return_value = fakeDonor("donor@test.com", {"donor", "donor@test.com", "liver", "hosptal1"})
    mock_recipient.return_value = fakeRecipient("recipient@test.com", {"recipient", "recipient@test.com", "liver", "hosptal2"})
    drview.request.method = 'POST'
    drview.request.form = mock_request_form({"username": "name", "type": "donor", "report": "report", "organ": ["liver", "heart"]})
    mock_vur.return_value = fakeViewUserReports("donor@test.com", "donor", "report")
    mock_send_file.return_value = "sent successfully"
    mock_bytesio.return_value = str.encode("sent successfully")
    assert drview.donorHospitalRequestPage("requestid") == "sent successfully"

@mock.patch.object(drview.umr, 'UpdateMedicalReports')
@mock.patch.object(drview, 'request')
@mock.patch.object(drview, 'render_template')
@mock.patch.object(drview, 'g')
@mock.patch.object(drview.binascii, 'hexlify')
@mock.patch.object(drview, 'flash')
@mock.patch.object(drview.ro, 'Recipient')
@mock.patch.object(drview.do, 'Donor')
@mock.patch.object(drview.rdo, 'OpenRequestDetails')
def test_donorHospitalRequestPage_upload_updated(mock_ord, mock_donor, mock_recipient, mock_flash,
                                         mock_binr, mock_g, mock_ren, mock_request, mock_umr):
    mock_ord.return_value = fakeOpenRequestDetails("requestid", [("donor@test.com", "recipient@test.com", "organ", "pending")])
    mock_donor.return_value = fakeDonor("donor@test.com", {"donor", "donor@test.com", "liver", "hosptal1"})
    mock_recipient.return_value = fakeRecipient("recipient@test.com", {"recipient", "recipient@test.com", "liver", "hosptal2"})
    drview.request.method = 'POST'
    drview.request.files = {"reports": open("test.txt", "w+")}
    drview.request.form = mock_request_form({"username": "name", "type": "donor", "upload": "upload", "organ": ["liver", "heart"]})
    mock_umr.return_value = fakeUpdateMedicalReports("donor@test.com", "reports", "donor", True)
    mock_flash.return_value = "Updated Successfully"
    mock_binr.return_value = "reports"
    mock_ren.return_value = "<h2>donor receiver request"
    assert drview.donorHospitalRequestPage("requestid") == "<h2>donor receiver request"

@mock.patch.object(drview.umr, 'UpdateMedicalReports')
@mock.patch.object(drview, 'request')
@mock.patch.object(drview, 'render_template')
@mock.patch.object(drview, 'g')
@mock.patch.object(drview.binascii, 'hexlify')
@mock.patch.object(drview, 'flash')
@mock.patch.object(drview.ro, 'Recipient')
@mock.patch.object(drview.do, 'Donor')
@mock.patch.object(drview.rdo, 'OpenRequestDetails')
def test_donorHospitalRequestPage_upload_not_updated(mock_ord, mock_donor, mock_recipient, mock_flash,
                                         mock_binr, mock_g, mock_ren, mock_request, mock_umr):
    mock_ord.return_value = fakeOpenRequestDetails("requestid", [("donor@test.com", "recipient@test.com", "organ", "pending")])
    mock_donor.return_value = fakeDonor("donor@test.com", {"donor", "donor@test.com", "liver", "hosptal1"})
    mock_recipient.return_value = fakeRecipient("recipient@test.com", {"recipient", "recipient@test.com", "liver", "hosptal2"})
    drview.request.method = 'POST'
    drview.request.files = {"reports": open("test.txt", "w+")}
    drview.request.form = mock_request_form({"username": "name", "type": "donor", "upload": "upload", "organ": ["liver", "heart"]})
    mock_umr.return_value = fakeUpdateMedicalReports("donor@test.com", "reports", "donor", False)
    mock_flash.return_value = "Insertion Error!"
    mock_binr.return_value = "reports"
    mock_ren.return_value = "<h2>donor receiver request"
    assert drview.donorHospitalRequestPage("requestid") == "<h2>donor receiver request"

@mock.patch.object(drview, 'request')
@mock.patch.object(drview, 'render_template')
@mock.patch.object(drview, 'g')
@mock.patch.object(drview, 'flash')
@mock.patch.object(drview.ro, 'Recipient')
@mock.patch.object(drview.do, 'Donor')
@mock.patch.object(drview.rdo, 'OpenRequestDetails')
def test_donorHospitalRequestPage_upload_invalidcerti(mock_ord, mock_donor, mock_recipient, mock_flash,
                                                       mock_g, mock_ren, mock_request):
    mock_ord.return_value = fakeOpenRequestDetails("requestid", [("donor@test.com", "recipient@test.com", "organ", "pending")])
    mock_donor.return_value = fakeDonor("donor@test.com", {"donor", "donor@test.com", "liver", "hosptal1"})
    mock_recipient.return_value = fakeRecipient("recipient@test.com", {"recipient", "recipient@test.com", "liver", "hosptal2"})
    drview.request.method = 'POST'
    drview.request.form = mock_request_form({"username": "name", "type": "donor", "upload": "upload", "reports": "reports", "organ": ["liver", "heart"]})
    mock_flash.return_value = "please insert a valid certificates"
    mock_ren.return_value = "<h2>donor receiver request</h2>"
    assert drview.donorHospitalRequestPage("requestid") == "<h2>donor receiver request</h2>"

@mock.patch.object(drview, 'redirect')
@mock.patch.object(drview, 'url_for')
@mock.patch.object(drview.uro, 'UpdateRequestStatus')
@mock.patch.object(drview, 'request')
@mock.patch.object(drview, 'render_template')
@mock.patch.object(drview, 'g')
@mock.patch.object(drview, 'flash')
@mock.patch.object(drview.ro, 'Recipient')
@mock.patch.object(drview.do, 'Donor')
@mock.patch.object(drview.rdo, 'OpenRequestDetails')
def test_donorHospitalRequestPage_submit(mock_ord, mock_donor, mock_recipient, mock_flash,
                                        mock_g, mock_ren, mock_request, mock_urs, mock_url_for, mock_redirect):
    mock_ord.return_value = fakeOpenRequestDetails("requestid", [("donor@test.com", "recipient@test.com", "organ", "pending")])
    mock_donor.return_value = fakeDonor("donor@test.com", {"donor", "donor@test.com", "liver", "hosptal1"})
    mock_recipient.return_value = fakeRecipient("recipient@test.com", {"recipient", "recipient@test.com", "liver", "hosptal2"})
    drview.request.method = 'POST'
    drview.request.form = mock_request_form({"username": "name", "type": "donor", "submit": "submit", "organ": ["liver", "heart"]})
    mock_urs.return_value = fakeUpdateRequestStatus("request", "requestid", "donor@test.com", "body", True, True)
    mock_flash.return_value = "Request Status updated successfully"
    mock_url_for.return_value = "http://url"
    mock_redirect.return_value = "<h2>hospital home</h2"
    assert drview.donorHospitalRequestPage("requestid") == "<h2>hospital home</h2"

@mock.patch.object(drview.uro, 'UpdateRequestStatus')
@mock.patch.object(drview, 'request')
@mock.patch.object(drview, 'render_template')
@mock.patch.object(drview, 'g')
@mock.patch.object(drview, 'flash')
@mock.patch.object(drview.ro, 'Recipient')
@mock.patch.object(drview.do, 'Donor')
@mock.patch.object(drview.rdo, 'OpenRequestDetails')
def test_donorHospitalRequestPage_submit_failed(mock_ord, mock_donor, mock_recipient, mock_flash,
                                        mock_g, mock_ren, mock_request, mock_urs):
    mock_ord.return_value = fakeOpenRequestDetails("requestid", [("donor@test.com", "recipient@test.com", "organ", "pending")])
    mock_donor.return_value = fakeDonor("donor@test.com", {"donor", "donor@test.com", "liver", "hosptal1"})
    mock_recipient.return_value = fakeRecipient("recipient@test.com", {"recipient", "recipient@test.com", "liver", "hosptal2"})
    drview.request.method = 'POST'
    drview.request.form = mock_request_form({"username": "name", "type": "donor", "submit": "submit", "organ": ["liver", "heart"]})
    mock_urs.return_value = fakeUpdateRequestStatus("request", "requestid", "donor@test.com", "body", False, False)
    mock_flash.return_value = "Error updating request status. Please try again later!"
    mock_ren.return_value = "<h2>donor receiver request</h2>"
    assert drview.donorHospitalRequestPage("requestid") == "<h2>donor receiver request</h2>"

@mock.patch.object(drview.mail, 'send')
@mock.patch.object(drview, 'request')
@mock.patch.object(drview, 'render_template')
@mock.patch.object(drview, 'g')
@mock.patch.object(drview, 'flash')
@mock.patch.object(drview.ro, 'Recipient')
@mock.patch.object(drview.do, 'Donor')
@mock.patch.object(drview.rdo, 'OpenRequestDetails')
def test_donorHospitalRequestPage_email(mock_ord, mock_donor, mock_recipient, mock_flash,
                                        mock_g, mock_ren, mock_request, mock_mailsend):
    mock_ord.return_value = fakeOpenRequestDetails("requestid", [("donor@test.com", "recipient@test.com", "organ", "pending")])
    mock_donor.return_value = fakeDonor("donor@test.com", {"donor", "donor@test.com", "liver", "hosptal1"})
    mock_recipient.return_value = fakeRecipient("recipient@test.com", {"recipient", "recipient@test.com", "liver", "hosptal2"})
    drview.request.method = 'POST'
    drview.request.form = mock_request_form({"username": "name", "type": "donor", "email": "email", "organ": ["liver", "heart"]})
    mock_flash.return_value = "Email Sent Successfully"
    mock_mailsend.return_value = "sent"
    mock_ren.return_value = "<h2>donor receiver request</h2>"
    assert drview.donorHospitalRequestPage("requestid") == "<h2>donor receiver request</h2>"


@mock.patch.object(drview, 'request')
@mock.patch.object(drview, 'render_template')
@mock.patch.object(drview, 'g')
@mock.patch.object(drview, 'flash')
@mock.patch.object(drview.ro, 'Recipient')
@mock.patch.object(drview.do, 'Donor')
@mock.patch.object(drview.rdo, 'OpenRequestDetails')
def test_donorHospitalRequestPage_nodata(mock_ord, mock_donor, mock_recipient, mock_flash, mock_g,
                                         mock_ren, mock_request):
    mock_ord.return_value = fakeOpenRequestDetails("requestid", [("donor@test.com", "recipient@test.com", "organ", "pending")])
    mock_donor.return_value = fakeDonor("donor@test.com", None)
    mock_recipient.return_value = fakeRecipient("recipient@test.com", None)
    drview.request.method = 'POST'
    mock_flash.return_value = "No donor/reciever available for this Request!"
    mock_ren.return_value = "<h2>donor receiver request</h2>"
    assert drview.donorHospitalRequestPage("requestid") == "<h2>donor receiver request</h2>"