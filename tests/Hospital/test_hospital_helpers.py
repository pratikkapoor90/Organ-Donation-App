from organdonationwebapp.models.SqlClient import SqlClient

class mock_sqlclient(SqlClient)  :
   def __init__(self, body=None):
       self.host = "host"
       self.port = 0000
       self.user = "user"
       self.password = "pass"
       self.connect_timeout = 00
       self.dbname = "db"
       self.cursor = None
       self.connection = None
       self.body = body
   def startDBConnection(self):
       self.cursor = mock_cursor()
       self.connection = mock_connection()
   def closeDBConnection(self):
       if(self.cursor):
           self.cursor.close()
       if(self.connection):
           self.connection.close()

class mock_db_results(object):
   def __init__(self, body):
       self.body = body
   def fetchall(self):
       return self.body

class mock_connection(object):
   def commit(self):
       pass
   def close(self):
       pass

class mock_cursor(object):
   def callproc(self, query, arguments):
       pass
   def close(self):
       pass
   def stored_results(self):
       return [mock_db_results("results"), mock_db_results("results2")]

class fakeHospital(object):
   def __init__(self):
       self.hospitalName = "hospitalName"
       self.emailID = "emailID"
       self.phone = "phone"
       self.address = "address"
       self.province = "province"
       self.city = "city"
       self.password = "password"
       self.data = "certificateFile"