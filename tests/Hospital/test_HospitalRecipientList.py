import mock
import logging
import organdonationwebapp.Hospital.HospitalRecipientList as hrlo


@mock.patch.object(hrlo.hc, 'getHospitalRecipientList')
def test_getRecipientList(mock_hospital_reclist):
    mock_hospital_reclist.return_value = [("Pratik", "Kapoor", "pratik.kapoor90@gmail.com", "Halifax"),("Test", "Test", "test@gmail.com", "Halifax")]
    hosRecipientList = hrlo.HospitalRecipientList("IWK",logging.getLogger())
    assert hosRecipientList.getRecipientList() == [("Pratik", "Kapoor", "pratik.kapoor90@gmail.com", "Halifax"),("Test", "Test", "test@gmail.com", "Halifax")]


@mock.patch.object(hrlo.hc, 'getHospitalRecipientList')
def test_getRecipientList_exception(mock_hospital_reclist):
    hosRecipientList = hrlo.HospitalRecipientList("",logging.getLogger())
    mock_hospital_reclist.side_effect = Exception("Hospital recipient list exception")
    hosRecipientList.getRecipientList()