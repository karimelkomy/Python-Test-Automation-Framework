import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.loginPage_locators = self.pageLocators('LoginPage')

    def isAt(self):
        header_login = self.getElementList(*self.locator(self.loginPage_locators, 'header_login'))
        if len(header_login) > 0:
            return True
        return False

    def login(self, email, password):
        self.sendKeys(email, *self.locator(self.loginPage_locators, 'input_email'))
        self.sendKeys(password, *self.locator(self.loginPage_locators, 'input_password'))
        self.elementClick(*self.locator(self.loginPage_locators, 'btn_login'))
