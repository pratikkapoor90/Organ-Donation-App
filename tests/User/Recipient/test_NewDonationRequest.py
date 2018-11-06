import mock
import logging
import organdonationwebapp.User.Recipient.NewDonationRequest as newdonationrequesttest

@mock.patch.object(newdonationrequesttest.ruc, 'createRequest')
def test_createDonationRequest_pass(mock_donation__create_req):
    mock_donation__create_req.return_value = True
    mock_donor_object = newdonationrequesttest.NewDonationRequest("donor@gmail.com","receipent@gmail.com","heart","iwk", logging.getLogger())
    assert mock_donor_object.createDonationRequest() == True

@mock.patch.object(newdonationrequesttest.ruc, 'createRequest')
def test_createDonationRequest_fail(mock_donation__create_req):
    mock_donation__create_req.return_value = False
    mock_donor_object = newdonationrequesttest.NewDonationRequest("donor@gmail.com","receipent@gmail.com","heart","iwk", logging.getLogger())
    assert mock_donor_object.createDonationRequest() == False

@mock.patch.object(newdonationrequesttest.ruc, 'createRequest')
def test_createDonationRequest_exception(mock_donation__create_req):
    mock_donation__create_req.side_effect = Exception("createRequest exception")
    mock_donor_object = newdonationrequesttest.NewDonationRequest("","","","", logging.getLogger())
    mock_donor_object.createDonationRequest()