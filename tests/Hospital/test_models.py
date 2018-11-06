import mock
import organdonationwebapp.Hospital.Models as hmod
from test_hospital_helpers import mock_sqlclient, fakeHospital

@mock.patch.object(hmod, 'SqlClient')
def test_hospitalRegistration(mock_sql):
   hmod.SqlClient = mock_sqlclient
   hmodel = hmod.HospitalModel()
   assert hmodel.hospitalRegistration(fakeHospital()) == True

@mock.patch.object(hmod.SqlClient, 'startDBConnection')
def test_hospitalRegistration_exception(mock_sql):
   mock_sql.side_effect = Exception()
   hmodel = hmod.HospitalModel()
   assert hmodel.hospitalRegistration(fakeHospital()) == False

def test_hospitalLoginAuthentication():
   hmod.SqlClient = mock_sqlclient
   hmodel = hmod.HospitalModel()
   assert hmodel.hospitalLoginAuthentication("email", "pass") == "results"