from pages.base_page import BasePage
from utils.locators import *


class RegisterPage(BasePage):

    def __init__(self, chrome_webdriver):
        super().__init__(chrome_webdriver)
        self.locator = RegisterPageLocator

    def create_new_account(self, name, email, password, confirmpassword):
        name_text_box = self.chrome_webdriver.find_element(*self.locator.USER_NAME_FIELD)
        name_text_box.send_keys(name)

        email_text_box = self.chrome_webdriver.find_element(*self.locator.EMAIL_FIELD)
        email_text_box.send_keys(email)

        password_text_box = self.chrome_webdriver.find_element(*self.locator.PASSWORD_FIELD)
        password_text_box.send_keys(password)

        re_password = self.chrome_webdriver.find_element(*self.locator.RE_ENTER_PASSWORD)
        re_password.send_keys(confirmpassword)

        button = self.chrome_webdriver.find_element(*self.locator.BUTTON)
        button.click()