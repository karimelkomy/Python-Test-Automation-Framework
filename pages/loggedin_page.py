import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class LoggedInPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.loggedInPage_locators = self.pageLocators('LoggedInPage')

    @property
    def isAt(self):
        input_search = self.getElementList(*self.locator(self.loggedInPage_locators, 'input_search'))
        if len(input_search) > 0:
            return True
        return False
