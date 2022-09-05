import pytest
import time
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random
from selenium.webdriver.common.keys import Keys

class Test_003_AddCustomer:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen() #Logger

    def test_addCustomer(self,setup):
        self.logger.info("*****Test_003_AddCustomer*********")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*******Login successful**********")

        self.logger.info("*******starting Add customer Test **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickonCustomerMenu()
        self.addcust.clickonCustomerMenuItem()
        self.addcust.clickOnAddNew()

        self.logger.info("*****Providing Customer Info***********")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerofVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Victor")
        self.addcust.setLastName("Charles")
        self.addcust.setDob("7/05/1985")
        self.addcust.setCustomerRoles("busyQA")
        self.addcust.setAdminContent("this is for testing.....")
        self.addcust.clickOnSave()

        self.logger.info("****** Saving Customer Info***********")

        self.logger.info("****** Add customer  validation started **********")

        self.msg = self.driver.find_element(By.TAG_NAME,"body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("*** Add customer test passed***")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer.png") #Screnshot
            self.logger.error("*** Add customer test failed***")
            assert True == False

        self.driver.close()
        self.logger.info("**Ending the page Home test *** ")

def random_generator(size = 8, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

