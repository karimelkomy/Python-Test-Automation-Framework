import time
import traceback
import random
import string
import utilities.custom_logger as cl
import logging


class Util(object):

    log = cl.customLogger(logging.DEBUG)

    def sleep(self, sec, info=""):
        """
        Put the program to wait for the specified amount of time
        """
        if info is not None:
            self.log.info("Wait :: " + str(sec) + " seconds for " + info)
            try:
                time.sleep(sec)
            except:
                traceback.print_stack()

    def getAlphaNumeric(self, length, type='letters'):
        """
        Get random string of characters
        :param length: Length of string, number of characters string should have
        :param type: Type of character string should have. Default is letters
        Provide lower/upper/digits for different types
        """
        alpha_num = ''
        if type == 'lower':
            case = string.ascii_lowercase
        elif type == 'upper':
            case = string.ascii_uppercase
        elif type == 'digits':
            case = string.digits
        elif type == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))

    def getUniqueName(self, charCount=10):
        """
        Get a unique name
        """
        return self.getAlphaNumeric(charCount, 'lower')

    def getUniqueNameList(self, listSize=5, itemLength=None):
        """
        Get a list of valid names

        :param listSize: Number of names. Default is 5 names in a list
        :param itemLength: It should be a list containing number of items equal to the list size
                            This determines the length of each item in the list -> [1, 2, 3, 4, 5]
        """
        nameList = []
        for i in range(0, listSize):
            nameList.append(self.getUniqueName(itemLength[i]))
        return nameList

    def verifyListMatch(self, expectedList, actualList):
        """
        Verify two list matches

        :param expectedList: Expected List
        :param actualList: Actual List
        """
        return set(expectedList) == set(actualList)

    def verifyListContains(self, expectedList, actualList):
        """
        Verify actual list contains elements of expected list

        :param expectedList: Expected List
        :param actualList: Actual List
        """
        length = len(expectedList)
        for i in range(0, length):
            if expectedList[i] not in actualList:
                return False
        else:
            return True

    def verifyTextContains(self, actualText, expectedText):
        """
        verify actual text contains expected text string

        :param actualText: Actual Text
        :param expectedText: Expected Text
        """
        self.log.info("Actual Text From Application Web UI --> :: " + actualText)
        self.log.info("Expected Text From Application Web UI --> :: " + expectedText)

        if expectedText.lower() in actualText.lower():
            self.log.info("### VERIFICATIONS CONTAINS !!!")
            return True
        else:
            self.log.error("### VERIFICATIONS DOES NOT CONTAINS !!!")

    def verifyTextMatch(self, actualText, expectedText):
        """
        verify text match

        :param actualText: Actual Text
        :param expectedText: Expected Text
        """
        self.log.info("Actual Text From Application Web UI --> :: " + actualText)
        self.log.info("Expected Text From Application Web UI --> :: " + expectedText)
        if expectedText.lower() == actualText.lower():
            self.log.info("### VERIFICATIONS MATCHED !!!")
            return True
        else:
            self.log.error("### VERIFICATIONS DOES NOT MATCHED !!!")


