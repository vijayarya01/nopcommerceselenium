import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
# from PIL import Image
# from Screenshot import Screenshot_clipping

class Test_001_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self,setup):

        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("*************** Verifying Home Page Title *****************")

        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*************** Home Page title case is passed *****************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("*************** Home Page title case is failed *****************")
            assert False





    def test_login(self,setup):
        self.logger.info("*************** Verifying the login test *****************")

        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        self.driver.close()

        if act_title == "Dashboard / nopCommerce administration":
            assert True

            # self.driver.close()

            self.logger.info("*************** login test case is passed *****************")

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            # self.driver.close()
            self.logger.error("*************** Login test is failed *****************")
            assert False





