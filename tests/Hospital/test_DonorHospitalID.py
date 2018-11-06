import mock
import organdonationwebapp.Hospital.DonorHospitalID as odh

@mock.patch.object(odh.hc, 'getHospitalID')
def test_getDonorHospitalID(mock_hospital_ID):
    mock_hospital_ID.return_value = ["pratik@gmail.com"]
    hosID = odh.DonorHospitalID("IWK")
    assert hosID.getDonorHospitalID() == ["pratik@gmail.com"]

@mock.patch.object(odh.hc, 'getHospitalID')
def test_getDonorHospitalID_nodata(mock_hospital_ID):
    mock_hospital_ID.return_value = None
    hosID = odh.DonorHospitalID("IWK")
    assert hosID.getDonorHospitalID() == None


@mock.patch.object(odh.hc, 'getHospitalID')
def test_getDonorHospitalID_exception(mock_hospital_ID):
    mock_hospital_ID.side_effect = Exception("hospital ID exception")
    hosID = odh.DonorHospitalID("")
    hosID.getDonorHospitalID()
