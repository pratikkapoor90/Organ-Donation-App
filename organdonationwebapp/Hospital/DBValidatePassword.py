from organdonationwebapp.Hospital.ValidatePassword import ValidatePassword
from organdonationwebapp import hc
import json
import re


REGEX_PATTERN = "[@_!#$%^&*()<>?/\|}{~:]"


class DBValidatePassword(ValidatePassword):

    def __init__(self, password):
        super(DBValidatePassword,self).__init__(password)
        self.ruleDict = self.parsePasswordRules()


    def parsePasswordRules(self):
        dbRule = hc.getPassword()
        dbRuleDict = {}
        for item in dbRule:
            dbRuleDict[item[0]] = int(item[1])
        return dbRuleDict


    def validateCapitalLetters(self):
        count=0
        if "capital_letters" not in self.ruleDict:
            return True
        for i in self.password:
            if(i.isupper()):
                count = count+1
        if(count != self.ruleDict["capital_letters"]):
            return False
        else:
            return True


    def validateSmallLetters(self):
        count=0
        if "small_letters" not in self.ruleDict:
            return True
        for i in self.password:
            if(i.islower()):
                count = count+1
        if(count != self.ruleDict["small_letters"]):
            return False
        else:
            return True


    def validateDigits(self):
        count=0
        if "digits" not in self.ruleDict:
            return True
        for i in self.password:
            if(i.isdigit()):
                count = count+1
        if(count != self.ruleDict["digits"]):
            return False
        else:
            return True


    def validateSpecialCharacters(self):
        if "special_characters" not in self.ruleDict:
            return True
        SpecialCharacters = re.compile(REGEX_PATTERN)
        match = re.findall(SpecialCharacters, self.password)
        if(len(match) != self.ruleDict["special_characters"]):
            return False
        else:
            return True