import mock
import logging
import organdonationwebapp.Hospital.HospitalRequestList as hreq


@mock.patch.object(hreq.hc, 'getHospitalRequestList')
def test_getPendingRequestList(mock_request_list):
    mock_request_list.return_value = [("test@gmail.com", "pratik.kapoor90@gmail.com", "liver")]
    hosHome = hreq.HospitalRequestList("iwk@gmail.com",logging.getLogger())
    assert hosHome.getPendingRequestList() == [("test@gmail.com", "pratik.kapoor90@gmail.com", "liver")]


@mock.patch.object(hreq.hc, 'getHospitalRequestList')
def test_getPendingRequestList_exception(mock_request_list):
    hosHome = hreq.HospitalRequestList("",logging.getLogger())
    mock_request_list.side_effect = Exception("Request list exception")
    hosHome.getPendingRequestList()