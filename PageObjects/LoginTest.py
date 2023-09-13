from selenium import webdriver
import pytest


class LoginTest:
    username_text_id = ""
    password_text_id = ""
    login_Btn = ""

    def __init__(self, driver):
        self.driver = driver


def setUsername(self, username):
    self.find_element_by_id(self.username_id).clear()
    self.fimnd_element_by_id(self.username_id).send_keys


def setPassword(self, password):
    self.find_element_by_id(self.password_id).clear()
    self.find_element_by_id(self.password_id).send_keys


def LoginBtn(self, Btn_Login):
    self.find_element_by_id(self.login_Btn).click()

