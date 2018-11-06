import mock
import logging
import organdonationwebapp.User.OpenRequestDetails as ored


@mock.patch.object(ored.uc, 'organRequest')
def test_getOpenRequestData(mock_user_organreq):
    mock_user_organreq.return_value = ["organ1", "organ2"]
    openReq = ored.OpenRequestDetails("request1",logging.getLogger())
    assert openReq.getOpenRequestData() == ["organ1", "organ2"]


@mock.patch.object(ored.uc, 'organRequest')
def test_getOpenRequestData_nodata(mock_user_organreq):
    mock_user_organreq.return_value = None
    openReq = ored.OpenRequestDetails("request1",logging.getLogger())
    assert openReq.getOpenRequestData() == None


@mock.patch.object(ored.uc, 'organRequest')
def test_getOpenRequestData_exception(mock_user_organreq):
    mock_user_organreq.side_effect = Exception("createRequest exception")
    openReq = ored.OpenRequestDetails("",logging.getLogger())
    openReq.getOpenRequestData()