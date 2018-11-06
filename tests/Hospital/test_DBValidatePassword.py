import mock
import organdonationwebapp.Hospital.DBValidatePassword as dbval


@mock.patch.object(dbval.DBValidatePassword, 'parsePasswordRules')
def test_validateCapitalLetters(mock_parsepassword):
    mock_parsepassword.return_value = {"capital_letters": 2}
    dbvalpass = dbval.DBValidatePassword("Password1P")
    assert dbvalpass.validateCapitalLetters() == True


@mock.patch.object(dbval.DBValidatePassword, 'parsePasswordRules')
def test_validateCapitalLetters_noval(mock_parsepassword):
    mock_parsepassword.return_value = {"": 2}
    dbvalpass = dbval.DBValidatePassword("Password1P")
    assert dbvalpass.validateCapitalLetters() == True


@mock.patch.object(dbval.DBValidatePassword, 'parsePasswordRules')
def test_validateCapitalLetters_failed(mock_parsepassword):
    mock_parsepassword.return_value = {"capital_letters": 4}
    dbvalpass = dbval.DBValidatePassword("Password1")
    assert dbvalpass.validateCapitalLetters() == False


@mock.patch.object(dbval.DBValidatePassword, 'parsePasswordRules')
def test_validateSmallLetters(mock_parsepassword):
    mock_parsepassword.return_value = {"small_letters": 5}
    dbvalpass = dbval.DBValidatePassword("passw")
    assert dbvalpass.validateSmallLetters() == True


@mock.patch.object(dbval.DBValidatePassword, 'parsePasswordRules')
def test_validateSmallLetters_noval(mock_parsepassword):
    mock_parsepassword.return_value = {"": 2}
    dbvalpass = dbval.DBValidatePassword("Password1P")
    assert dbvalpass.validateSmallLetters() == True


@mock.patch.object(dbval.DBValidatePassword, 'parsePasswordRules')
def test_validateSmallLetters_failed(mock_parsepassword):
    mock_parsepassword.return_value = {"small_letters": 5}
    dbvalpass = dbval.DBValidatePassword("password")
    assert dbvalpass.validateSmallLetters() == False


@mock.patch.object(dbval.DBValidatePassword, 'parsePasswordRules')
def test_validateDigits(mock_parsepassword):
    mock_parsepassword.return_value = {"digits": 3}
    dbvalpass = dbval.DBValidatePassword("password123")
    assert dbvalpass.validateDigits() == True


@mock.patch.object(dbval.DBValidatePassword, 'parsePasswordRules')
def test_validateDigits_noval(mock_parsepassword):
    mock_parsepassword.return_value = {"": 2}
    dbvalpass = dbval.DBValidatePassword("Password1P")
    assert dbvalpass.validateDigits() == True


@mock.patch.object(dbval.DBValidatePassword, 'parsePasswordRules')
def test_validateDigits_failed(mock_parsepassword):
    mock_parsepassword.return_value = {"digits": 3}
    dbvalpass = dbval.DBValidatePassword("password1")
    assert dbvalpass.validateDigits() == False


@mock.patch.object(dbval.DBValidatePassword, 'parsePasswordRules')
def test_validateSpecialCharacters(mock_parsepassword):
    mock_parsepassword.return_value = {"special_characters": 3}
    dbvalpass = dbval.DBValidatePassword("password***")
    assert dbvalpass.validateSpecialCharacters() == True


@mock.patch.object(dbval.DBValidatePassword, 'parsePasswordRules')
def test_validateSpecialCharacters_noval(mock_parsepassword):
    mock_parsepassword.return_value = {"": 2}
    dbvalpass = dbval.DBValidatePassword("Password1P")
    assert dbvalpass.validateSpecialCharacters() == True


@mock.patch.object(dbval.DBValidatePassword, 'parsePasswordRules')
def test_validateSpecialCharacters_failed(mock_parsepassword):
    mock_parsepassword.return_value = {"special_characters": 3}
    dbvalpass = dbval.DBValidatePassword("password!")
    assert dbvalpass.validateSpecialCharacters() == False