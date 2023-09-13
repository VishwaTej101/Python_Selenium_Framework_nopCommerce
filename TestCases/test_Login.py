from selenium import webdriver
import pytest
from PythonSelenium_Framework import PageObjects
import LoginPage

class Test_001_Login:

    baseURL=""
    username=""
    password=""

    def test_homePageTitle(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "":
            assert True
        else:
            assert False
    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.usernam)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin()
        act_title = self.driver.title
        self.driver.close()

        if act_title == "":
             assert True
        else:
            assert False

