import mock
import logging
import organdonationwebapp.User.Donor.Donor as donor

@mock.patch.object(donor.duc, 'donorHospitalShowDonorProfile')
def test_donorHospitalRequestPage_pass(mock_donormail):
    mock_donormail.return_value = [("pratik","Kapoor","pratik@gmail.com"),("shivkumar","jaiswal","shivsj1402@gmail.com")]
    donorobj = donor.Donor("abc@gmail.com",logging.getLogger())
    assert donorobj.donorHospitalRequestPage() == [("pratik","Kapoor","pratik@gmail.com"),("shivkumar","jaiswal","shivsj1402@gmail.com")]

@mock.patch.object(donor.duc, 'donorHospitalShowDonorProfile')
def test_donorHospitalRequestPage_fail(mock_donormail):
    mock_donormail.return_value = None
    donorobj = donor.Donor("abc@gmail.com",logging.getLogger())
    assert donorobj.donorHospitalRequestPage()  == None

@mock.patch.object(donor.duc, 'donorHospitalShowDonorProfile')
def test_donorHospitalRequestPage_execption(mock_donormail):
    mock_donormail.side_effect = Exception("createRequest exception")
    donorobj = donor.Donor("",logging.getLogger())
    donorobj.donorHospitalRequestPage()