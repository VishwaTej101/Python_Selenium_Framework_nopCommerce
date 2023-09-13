import pytest
from selenium import webdriver
from PythonSelenium_Framework.PageObjects.LoginTest import LoginTest

class Test_001_Login:
    baseURL = ""
    username= ""
    password= ""

def test_HomePageTitle(self):
    driver = webdriver.Chrome()
    self.driver.get(self.baseURL)
    act_title=self.driver.title

    if(act_title==""):
        assert True
    else:
        assert False
def test_Login(self):
    self.driver = webdriver.Chrome()
    self.driver.get(self.baseURL)
    self.lp = LoginPage(self.driver)
    self.lp.setUsername(self.username)
    self.lp.setPassword(self.password)
    self.lp.LoginBtn()
    login_title=self.driver.title
    if(login_title==""):
        assert True
    else:
        assert False
