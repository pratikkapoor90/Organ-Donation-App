import mock
import logging
import organdonationwebapp.User.Donor.ShowDonorRequestStatus as donorstatus


request_status_data = [
    ("aitem", "aitem", "aitem", "aitem", "aitem", 1),
    ("aitem", "aitem", "aitem", "aitem", "aitem", 1),
    ("pitem", "pitem", "pitem", "pitem", "pitem", 0),
    ("pitem", "pitem", "pitem", "pitem", "pitem", 0),
    ("noitem", "noitem", "noitem", "noitem", "noitem", ""),
    ("noitem", "noitem", "noitem", "noitem", "noitem", "")
]

request_data = {
    "approved": [("aitem", "aitem", "aitem", "aitem", "aitem", 1),
                 ("aitem", "aitem", "aitem", "aitem", "aitem", 1)],
    "pending": [("pitem", "pitem", "pitem", "pitem", "pitem", 0),
                ("pitem", "pitem", "pitem", "pitem", "pitem", 0),
                ("noitem", "noitem", "noitem", "noitem", "noitem", ""),
                ("noitem", "noitem", "noitem", "noitem", "noitem", "")]
}


@mock.patch.object(donorstatus.duc, 'getOpenRequestsStatus')
def test_getRequestsStatus(mock_donorstatus):
    mock_donorstatus.return_value = request_status_data
    donorobj = donorstatus.ShowDonorRequestStatus("user1@test.com", "user2@test.com", logging.getLogger())
    assert donorobj.getRequestsStatus() == request_data


@mock.patch.object(donorstatus.duc, 'getOpenRequestsStatus')
def test_getRequestsStatus_nodata(mock_donorstatus):
    mock_donorstatus.return_value = []
    donorobj = donorstatus.ShowDonorRequestStatus("user1@test.com", "user2@test.com",logging.getLogger())
    assert donorobj.getRequestsStatus() == {"approved": [], "pending": []}


@mock.patch.object(donorstatus.duc, 'getOpenRequestsStatus')
def test_getRequestsStatus_exception(mock_donorstatus):
    mock_donorstatus.side_effect = Exception("db error")
    donorobj = donorstatus.ShowDonorRequestStatus("user1@test.com", "user2@test.com",logging.getLogger())
    assert str(donorobj.getRequestsStatus()) == "db error"