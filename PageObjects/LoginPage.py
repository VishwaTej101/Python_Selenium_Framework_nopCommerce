from selenium import webdriver


class LoginPage:
    textbox_username_id = ""
    textbox_password_id = ""
    button_login_xpath = ""

    link_logout_linkText = ""

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_elment_by_id(self.textbox_username_id).clear()
        self.driver.find_elment_by_id(self.textbox_username_id).send_keys(username)

    def Setpassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_elment_by_id(self.textbox_password_id).send_keys(password)

    def ClickLogin(self):
        self.driver.find_elment_by_xpath(self.button_login_xpath).click()

    def ClickLogout(self):
        self.driver.find_elment_by_link_text(self.link_text().click())


