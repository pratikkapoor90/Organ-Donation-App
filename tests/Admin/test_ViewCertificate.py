import mock
import logging
import organdonationwebapp.Admin.ViewCertificate as admincertificate

@mock.patch.object(admincertificate.ac, 'getHospitalCertificate')
def test_ValidateHospital_pass(mock_admincertificate):
    mock_admincertificate.return_value = True
    adminobj = admincertificate.ViewCertificate("hpratik@gmail.com",logging.getLogger())
    assert adminobj.getHospitalCerti() ==True

@mock.patch.object(admincertificate.ac, 'getHospitalCertificate')
def test_ValidateHospital_fail(mock_admincertificate):
    mock_admincertificate.return_value = None
    adminobj = admincertificate.ViewCertificate("hpratik@gmail.com",logging.getLogger())
    assert adminobj.getHospitalCerti()  == None

@mock.patch.object(admincertificate.ac, 'getHospitalCertificate')
def test_ValidateHospital_execption(mock_admincertificate):
    mock_admincertificate.side_effect = Exception("createRequest exception")
    adminobj = admincertificate.ViewCertificate("",logging.getLogger())
    adminobj.getHospitalCerti()