import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_SearchCustomerByEmail_004:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen() #Logger

    def test_SearchCustomerByEmail(self,setup):
        self.logger.info("*******test_SearchCustomerByEmail_004 **********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********LoginSuccessful***********")

        self.logger.info("*********Starting Search Customer By Email*************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickonCustomerMenu()
        self.addcust.clickonCustomerMenuItem()

        self.logger.info("*******searching customer by Email id")

        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()

        time.sleep(5)
        status = searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True ==status
        self.logger.info("*******TC_SearchCustomerByEmail_004 Finished**********")

        