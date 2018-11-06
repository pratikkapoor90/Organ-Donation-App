import mock
import logging
import organdonationwebapp.User.ViewUserReports as vur

@mock.patch.object(vur.uc, 'getReports')
def test_viewReports(mock_user_getreports):
    mock_user_getreports.return_value = "userreports"
    userReports = vur.ViewUserReports("user1@test.com", "donor", logging.getLogger())
    assert userReports.viewReports() == "userreports"

@mock.patch.object(vur.uc, 'getReports')
def test_viewReports_noresult(mock_user_getreports):
    mock_user_getreports.return_value = None
    userReports = vur.ViewUserReports("user1@test.com", "donor", logging.getLogger())
    assert userReports.viewReports() == None

@mock.patch.object(vur.uc, 'getReports')
def test_viewReports_exception(mock_user_getreports):
    mock_user_getreports.side_effect = Exception("createRequest exception")
    userReports = vur.ViewUserReports("", "", logging.getLogger())
    userReports.viewReports()