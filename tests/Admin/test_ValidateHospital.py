import mock
import logging
import organdonationwebapp.Admin.ValidateHospital as adminvalidate

@mock.patch.object(adminvalidate.ac, 'validateHospital')
def test_ValidateHospital_pass(mock_adminvalidate):
    mock_adminvalidate.return_value = True
    adminobj = adminvalidate.ValidateHospital({'validate': 'hpratik@gmail.com '},logging.getLogger())
    assert adminobj.updateValidateHospitalFlag() ==True

@mock.patch.object(adminvalidate.ac, 'validateHospital')
def test_ValidateHospital_fail(mock_adminvalidate):
    mock_adminvalidate.return_value = False
    adminobj = adminvalidate.ValidateHospital({'validate': 'somehospital@gmail.com '},logging.getLogger())
    assert adminobj.updateValidateHospitalFlag()  == False

@mock.patch.object(adminvalidate.ac, 'validateHospital')
def test_ValidateHospital_execption(mock_adminvalidate):
    mock_adminvalidate.side_effect = Exception("createRequest exception")
    adminobj = adminvalidate.ValidateHospital("",logging.getLogger())
    adminobj.updateValidateHospitalFlag()