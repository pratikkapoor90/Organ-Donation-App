import mock
import logging
import organdonationwebapp.User.Donor.ShowDonorProfile as donorshowprofile

@mock.patch.object(donorshowprofile.duc, 'donorHospitalShowDonorProfile')
def test_getDonorProfile_pass(mock_donorprofile):
    mock_donorprofile.return_value = [("pratik","Kapoor","pratik@gmail.com"),("shivkumar","jaiswal","shivsj1402@gmail.com")]
    donorobj = donorshowprofile.ShowDonorProfile("abc@gmail.com",logging.getLogger())
    assert donorobj.getDonorProfile() == [("pratik","Kapoor","pratik@gmail.com"),("shivkumar","jaiswal","shivsj1402@gmail.com")]

@mock.patch.object(donorshowprofile.duc, 'donorHospitalShowDonorProfile')
def test_getDonorProfile_fail(mock_donorprofile):
    mock_donorprofile.return_value = None
    donorobj = donorshowprofile.ShowDonorProfile("abc@gmail.com",logging.getLogger())
    assert donorobj.getDonorProfile()  == None

@mock.patch.object(donorshowprofile.duc, 'donorHospitalShowDonorProfile')
def test_getDonorProfile_execption(mock_donorprofile):
    mock_donorprofile.side_effect = Exception("createRequest exception")
    donorobj = donorshowprofile.ShowDonorProfile("",logging.getLogger())
    donorobj.getDonorProfile()


@mock.patch.object(donorshowprofile.duc, 'showDonorOrgan')
def test_getDonorOrgans_pass(mock_donororgan):
    mock_donororgan.return_value = [("Liver",),("Heart",)]
    donorobj = donorshowprofile.ShowDonorProfile("abc@gmail.com",logging.getLogger())
    assert donorobj.getDonorOrgans() == [("Liver",),("Heart",)]

@mock.patch.object(donorshowprofile.duc, 'showDonorOrgan')
def test_getDonorOrgans_fail(mock_donororgan):
    mock_donororgan.return_value = None
    donorobj = donorshowprofile.ShowDonorProfile("abc@gmail.com",logging.getLogger())
    assert donorobj.getDonorOrgans()  == None

@mock.patch.object(donorshowprofile.duc, 'showDonorOrgan')
def test_getDonorOrgans_execption(mock_donororgan):
    mock_donororgan.side_effect = Exception("createReques exception")
    donorobj = donorshowprofile.ShowDonorProfile("",logging.getLogger())
    donorobj.getDonorOrgans()
