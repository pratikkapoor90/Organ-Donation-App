import abc

class ValidatePassword(abc.ABC):
    def __init__(self, password):
        self.password = password


    @abc.abstractmethod
    def validateCapitalLetters(self):
        pass

    @abc.abstractmethod
    def validateSmallLetters(self):
        pass

    @abc.abstractmethod
    def validateDigits(self):
        pass

    @abc.abstractmethod
    def validateSpecialCharacters(self):
        pass

    @abc.abstractmethod
    def parsePasswordRules(self):
        pass


    def isValid(self):
        if(self.validateCapitalLetters() and self.validateSmallLetters() and self.validateDigits() and self.validateSpecialCharacters()):
            return True
        else:
            return False