import mock
import logging
import organdonationwebapp.Hospital.HospitalList as hlo
import organdonationwebapp.API.Logger as logger


@mock.patch.object(hlo.hc, 'getHospitalList')
def test_getGlobalHospitalList(mock_hospital_list):
    mock_hospital_list.return_value = [("IWK", "iwk@gmail.com", "Queen Street"),("IWK", "iwk@gmail.com", "Queen Street")]
    hosList = hlo.HospitalList(logging.getLogger())
    assert hosList.getGlobalHospitalList() == [("IWK", "iwk@gmail.com", "Queen Street"),("IWK", "iwk@gmail.com", "Queen Street")]


@mock.patch.object(hlo.hc, 'getHospitalList')
def test_getGlobalHospitalList_nodata(mock_hospital_list):
    mock_hospital_list.return_value = None
    hosList = hlo.HospitalList(logging.getLogger())
    assert hosList.getGlobalHospitalList() == None


@mock.patch.object(hlo.hc, 'getHospitalList')
def test_getGlobalHospitalList_exception(mock_hospital_home):
    hosList = hlo.HospitalList(logging.getLogger())
    mock_hospital_home.side_effect = Exception("Hospital name exception")
    assert str(hosList.getGlobalHospitalList()) == 'Hospital name exception'