from utilities.teststatus import TestStatus
from navigation.homeNavigation import HomeNavigation
from pages.login_page import LoginPage
from pages.loggedin_page import LoggedInPage
import test_data.testData as td
import unittest
import pytest
import sys
import allure
from pytest_testrail.plugin import pytestrail

sys.path.insert(0, '../..')


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.homeNavigation = HomeNavigation(self.driver)
        self.loginPage = LoginPage(self.driver)
        self.loggedInPage = LoggedInPage(self.driver)
        self.ts = TestStatus(self.driver)

    # @pytest.mark.run(order=1)
    @allure.story('epic_1') # epic/story of the test case
    @allure.severity(allure.severity_level.MINOR) # severity of the test case
    # @pytestrail.case('C48') # test case if on TestRail
    def test_login_successfully(self):
        with allure.step('Navigate to login page'):
            self.homeNavigation.goToLoginPage()
            self.ts.markFinal(self.loginPage.isAt, "navigation to login page failed")

        with allure.step('Login'):
            self.loginPage.login(email=td.testData("email"), password=td.testData("password"))
            self.ts.markFinal(self.loggedInPage.isAt, "login failed")
