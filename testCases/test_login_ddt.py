import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from selenium.webdriver.common.keys import Keys
from utilities.customLogger import LogGen
from utilities import XLUtils
# from PIL import Image
# from Screenshot import Screenshot_clipping

class Test_002_DDT_Login:
    baseUrl = ReadConfig.getApplicationUrl()
    path = ".//TestData/LoginData.xlsx"

    logger = LogGen.loggen()

    def test_login_ddt(self,setup):
        self.logger.info("**********test _002_ddt_login_********")
        self.logger.info("*************** Verifying the login DDT test *****************")

        self.driver = setup
        self.driver.get(self.baseUrl)

        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of Rows in a Excel", self.rows)

        list_status = [] #Empty list variable

        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path,'Sheet1',r,2)
            self.exp = XLUtils.readData(self.path,'Sheet1',r,3)

            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*******Test is passed***********")
                    self.lp.clickLogout()
                    list_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("****** Test is failed******")
                    self.lp.clickLogout()
                    list_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("*******Test is failed***********")
                    self.lp.clickLogout()
                    list_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("****** Test is Passed******")
                    self.lp.clickLogout()
                    list_status.append("Pass")
        if "Fail" not in list_status:
            # self.logger.info("********LoginDDT test is passed*********")
            # self.driver.close()
            assert True
        else:
            # self.logger.info("******LoginDDt test is failed.")
            # self.driver.close()
            assert False

        self.logger.info("******End of LoginDDT test.************")
        self.logger.info("******Completed TC_LoingDDT_002************")





