import mock
import logging
import organdonationwebapp.Hospital.HospitalHome as hho


@mock.patch.object(hho.hc, 'getHospitalName')
def test_getHospitalName(mock_hospital_home):
    mock_hospital_home.return_value = [("IWK", "pratik.kapoor90@gmail.com")]
    hosHome = hho.HospitalHome("request1",logging.getLogger())
    assert hosHome.getHospitalName() == ("IWK", "pratik.kapoor90@gmail.com")


@mock.patch.object(hho.hc, 'getHospitalName')
def test_getHospitalName_nodata(mock_hospital_home):
    mock_hospital_home.return_value = None
    hosHome = hho.HospitalHome("request1",logging.getLogger())
    assert hosHome.getHospitalName() == None


@mock.patch.object(hho.hc, 'getHospitalName')
def test_getHospitalName_exception(mock_hospital_home):
    hosHome = hho.HospitalHome("",logging.getLogger())
    mock_hospital_home.side_effect = Exception("Hospital name exception")
    assert str(hosHome.getHospitalName()) == "Hospital name exception"