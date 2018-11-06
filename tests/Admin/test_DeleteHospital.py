import mock
import logging
import organdonationwebapp.Admin.DeleteHospital as admindelete

@mock.patch.object(admindelete.ac, 'deleteHospital')
def test_deleteHospital_pass(mock_deleteHosp):
    mock_deleteHosp.return_value = True
    adminobj = admindelete.DeleteHospital("iwk@gmail.com",logging.getLogger())
    assert adminobj.deleteHospital() ==True

@mock.patch.object(admindelete.ac, 'deleteHospital')
def test_deleteHospital_fail(mock_deleteHosp):
    mock_deleteHosp.return_value = False
    adminobj = admindelete.DeleteHospital("iwk@gmail.com",logging.getLogger())
    assert adminobj.deleteHospital()  == False

@mock.patch.object(admindelete.ac, 'deleteHospital')
def test_deleteHospital_exeption(mock_deleteHosp):
    mock_deleteHosp.side_effect = Exception("createRequest exception")
    adminobj = admindelete.DeleteHospital("",logging.getLogger())
    adminobj.deleteHospital()
