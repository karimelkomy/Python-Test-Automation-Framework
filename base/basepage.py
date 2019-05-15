from base.selenium_driver import SeleniumDriver
from traceback import print_stack
from utilities.util import Util
import utilities.read_json as RJ
import os


class BasePage(SeleniumDriver):

    def __init__(self, driver):
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def pageLocators(self, page):
        """
        read the locators of specific page
        :param page: page
        :return: list of all locators in specific page
        """
        locatorsPath = os.path.abspath("./locators/locators.json")
        locatorsJsonFile = RJ.readJson(locatorsPath)
        pageLocators = [locator for locator in locatorsJsonFile if locator['pageName'] in page]
        return pageLocators

    def locator(self, pageLocators, locatorName):
        """
        get specific locator in specific page
        :param pageLocators: specific page
        :param locatorName: locator name
        :return: locator and locator Type
        """
        for locator in pageLocators:
            if locatorName == locator['name']:
                return locator['locator'], locator['locateUsing']

    def verifyPageTitle(self, titleToVerify):
        """
        Verify the page Title

        :param titleToVerify: Title on the page that needs to be verified
        """
        try:
            actualTitle = self.getTitle()
            return  self.util.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False

