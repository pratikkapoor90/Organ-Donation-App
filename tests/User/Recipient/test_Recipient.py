import mock
import logging
import organdonationwebapp.User.Recipient.Recipient as recipient


@mock.patch.object(recipient.ruc, 'donorHospitalShowReceiverProfile')
def test_donorHospitalPageRecipientList(mock_recipientmail):
    mock_recipientmail.return_value = [("pratik","Kapoor","pratik@gmail.com"),("shivkumar","jaiswal","shivsj1402@gmail.com")]
    recipientobj = recipient.Recipient("abc@gmail.com",logging.getLogger())
    assert recipientobj.donorHospitalPageRecipientList() == [("pratik","Kapoor","pratik@gmail.com"),("shivkumar","jaiswal","shivsj1402@gmail.com")]

@mock.patch.object(recipient.ruc, 'donorHospitalShowReceiverProfile')
def test_donorHospitalPageRecipientList_nodata(mock_recipientmail):
    mock_recipientmail.return_value = None
    recipientobj = recipient.Recipient("someuser@gmail.com", logging.getLogger())
    assert recipientobj.donorHospitalPageRecipientList() == None

@mock.patch.object(recipient.ruc, 'donorHospitalShowReceiverProfile')
def test_donorHospitalPageRecipientList_exception(mock_recipientmail,):
    mock_recipientmail.side_effect = Exception("createRequest exception")
    recipientobj = recipient.Recipient("", logging.getLogger())
    recipientobj.donorHospitalPageRecipientList()