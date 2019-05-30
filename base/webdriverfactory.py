"""
@package base

WebDriver Factory class implementation
It creates a web-driver instance based on browser configurations

"""
from selenium import webdriver
import os
import test_data.testData as td


class WebDriverFactory:

    def __init__(self):
        """
        Inits WebDriverFactory class
        :Returns None:
        """
        self.browser = td.testData("browser")
        self.baseUrl = td.testData("environment")

    def getWebDriverInstance(self):
        """
        Get WebDriver Instance based on the browser configuration

        :return 'WebDriver Instance':
        """

        if self.browser == "firefox":
            driver = webdriver.Firefox()

        elif self.browser == "chrome":
            # Set Chrome driver
            driverLocation = "/users/karimelkomy/PycharmProjects/lib/chromedriver"
            os.environ["webdriver.chrome.driver"] = driverLocation
            driver = webdriver.Chrome(driverLocation)
            driver.set_window_size(1366, 768)

        else:
            driver = webdriver.Firefox()

        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(15)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(self.baseUrl)

        return driver


