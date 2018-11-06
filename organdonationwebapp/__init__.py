# Get flask
from flask import Flask
# Create the app
app = Flask(__name__)
app.debug=True


from organdonationwebapp.models.SqlClient import SqlClient
sc = None
if not sc:
    sc = SqlClient()


from organdonationwebapp.Admin.Models import AdminModel
ac = None
if not ac:
    ac = AdminModel()


from organdonationwebapp.Hospital.Models import HospitalModel
hc = None
if not hc:
    hc = HospitalModel()


from organdonationwebapp.User.Models import UserModel
uc = None
if not uc:
    uc = UserModel()


from organdonationwebapp.User.Donor.Models import DonorModel
duc = None
if not duc:
    duc = DonorModel()


from organdonationwebapp.User.Recipient.Models import RecipientModel
ruc = None
if not ruc:
    ruc = RecipientModel()

    

app.secret_key = 'lfjsdlkfjdklsjfkl'
app.config['SESSION'] = True
import organdonationwebapp.API.AdminViews
import organdonationwebapp.API.HospitalViews
import organdonationwebapp.API.DonorRecipientViews
import organdonationwebapp.API.RecipientViews
import organdonationwebapp.API.DonorViews
import organdonationwebapp.API.views

