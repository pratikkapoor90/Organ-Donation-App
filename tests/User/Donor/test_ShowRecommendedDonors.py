import mock
import logging
import organdonationwebapp.User.Donor.ShowRecommendedDonors as donorrecommended

@mock.patch.object(donorrecommended.duc, 'recommendedDonorList')
def test_ShowRecommendedDonors_pass(mock_donorrecommended):
    mock_donorrecommended.return_value = [("pratik","Kapoor","pratik@gmail.com"),("shivkumar","jaiswal","shivsj1402@gmail.com")]
    donorobj = donorrecommended.ShowRecommendedDonors("liver",logging.getLogger())
    assert donorobj.getrecommendedDonorList() ==[("pratik","Kapoor","pratik@gmail.com"),("shivkumar","jaiswal","shivsj1402@gmail.com")]

@mock.patch.object(donorrecommended.duc, 'recommendedDonorList')
def test_ShowRecommendedDonors_fail(mock_donorrecommended):
    mock_donorrecommended.return_value = None
    donorobj = donorrecommended.ShowRecommendedDonors("liver",logging.getLogger())
    assert donorobj.getrecommendedDonorList()  == None

@mock.patch.object(donorrecommended.duc, 'recommendedDonorList')
def test_ShowRecommendedDonors_execption(mock_donorrecommended):
    mock_donorrecommended.side_effect = Exception("createRequest exception")
    donorobj = donorrecommended.ShowRecommendedDonors("",logging.getLogger())
    donorobj.getrecommendedDonorList()

