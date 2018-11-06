import mock
import logging
import organdonationwebapp.User.Donor.DonorListDetails as donorlist


@mock.patch.object(donorlist.duc, 'getDonorList')
def test_getDonorsList_pass(mock_donorlist):
    mock_donorlist.return_value = [("pratik","Kapoor","pratik@gmail.com"),("shivkumar","jaiswal","shivsj1402@gmail.com")]
    donorobj = donorlist.DonorListDetails("abc@gmail.com",logging.getLogger())
    assert donorobj.getDonorsList("ABC hospital",logging.getLogger()) == [("pratik","Kapoor","pratik@gmail.com"),("shivkumar","jaiswal","shivsj1402@gmail.com")]

@mock.patch.object(donorlist.duc, 'getDonorList')
def test_getDonorsList_fail(mock_donorlist):
    mock_donorlist.return_value = None
    donorobj = donorlist.DonorListDetails("abc@gmail.com",logging.getLogger())
    assert donorobj.getDonorsList("ABC hospital",logging.getLogger())  == None

@mock.patch.object(donorlist.duc, 'getDonorList')
def test_getDonorsList_execption(mock_donorlist):
    mock_donorlist.side_effect = Exception("createRequest exception")
    donorobj = donorlist.DonorListDetails("",logging.getLogger())
    donorobj.getDonorsList("",logging.getLogger())