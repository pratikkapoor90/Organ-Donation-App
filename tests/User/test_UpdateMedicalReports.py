import mock
import logging
import organdonationwebapp.User.UpdateMedicalReports as umr

@mock.patch.object(umr.uc, 'updateReport')
def test_updateReports(mock_user_updatereport):
    mock_user_updatereport.return_value = True
    userReports = umr.UpdateMedicalReports("user1@test.com", "donor","reports",logging.getLogger())
    assert userReports.updateReports() == True

@mock.patch.object(umr.uc, 'updateReport')
def test_updateReports_failed(mock_user_updatereport):
    mock_user_updatereport.return_value = False
    userReports = umr.UpdateMedicalReports("user1@test.com", "donor", "reports",logging.getLogger())
    assert userReports.updateReports() == False

@mock.patch.object(umr.uc, 'updateReport')
def test_updateReports_exception(mock_user_updatereport):
    mock_user_updatereport.side_effect = Exception("createRequest exception")
    userReports = umr.UpdateMedicalReports("", "", "",logging.getLogger())
    userReports.updateReports()
