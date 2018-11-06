import mock
import organdonationwebapp.User.User as user
import organdonationwebapp.API.Logger as logger

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
    "organ": "liver"
}

@mock.patch.object(user.uc, 'userRegistration')
@mock.patch.object(user, 'url_for')
@mock.patch.object(logger, 'MyLogger')
def test_register(mock_logger, mock_url_for, mock_user_reg):
    aUser = user.User()
    aUser.initialize(user_json)
    aUser.setLogger(mock_logger)
    mock_url_for.return_value = "http://url"
    mock_user_reg.return_value = True
    assert aUser.register() == (True, "http://url")


@mock.patch.object(user.uc, 'userRegistration')
@mock.patch.object(logger, 'MyLogger')
def test_register_failed(mock_logger, mock_user_reg):
    aUser = user.User()
    aUser.initialize(user_json)
    aUser.setLogger(mock_logger)
    mock_user_reg.return_value = False
    assert aUser.register() == (False, "Registration Failed.")


@mock.patch.object(user.uc, 'userRegistration')
@mock.patch.object(logger, 'MyLogger')
def test_register_exception(mock_logger, mock_user_reg):
    aUser = user.User()
    aUser.initialize(user_json)
    aUser.setLogger(mock_logger)
    mock_user_reg.side_effect = Exception("register exception")
    aUser.register()


@mock.patch.object(logger, 'MyLogger')
def test_setlogger(mock_logger):
    aUser = user.User()
    aUser.setLogger(mock_logger)


def test_login():
    aUser = user.User()
    assert aUser.login() == NotImplementedError


@mock.patch.object(logger, 'MyLogger')
def test_build_User(mock_logger):
    aUser = user.User()
    aUser.initialize(user_json)
    aUser.setLogger(logger)
    assert type(user.build_User(user.User, user_json, logger)).__name__ == type(aUser).__name__