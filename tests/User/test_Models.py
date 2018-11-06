import mock
import organdonationwebapp.User.Models as model

user_json = {
    "first_name": "first",
    "last_name": "last",
    "phone_number": "1234",
    "email": "user1@test.com",
    "sex": "M",
    "dob": "01012010",
    "address": "user1 address",
    "province": "province",
    "city": "city",
    "hname": "hospital",
    "bloodgroup": "AB+",
    "usertype": "donor",
    "organ": ["liver", "heart"]
}

class mock_object(object):
    def __init__(self, *request_info, **kwargs):
        for d in request_info:
            for key in d:
                setattr(self, key, d[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])

@mock.patch.object(model.SqlClient, 'startDBConnection')
def test_userRegistration_noorgans(mock_start_db):
    user_json["organ"] = []
    mock_start_db.return_value = None
    usermodel = model.UserModel()
    assert usermodel.userRegistration(mock_object(user_json)) == True

@mock.patch.object(model.SqlClient, 'startDBConnection')
def test_userRegistration(mock_start_db):
    usermodel = model.UserModel()
    assert usermodel.userRegistration(mock_object(user_json)) == True
