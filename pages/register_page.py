from selenium.webdriver import Keys

from pages.base_page import BasePage
from files.sample_data import SampleData
from utils.locators import *


class RegisterPage(BasePage):

    def __init__(self, chrome_webdriver):
        super().__init__(chrome_webdriver)
        self.locator = RegisterPageLocator

    def create_new_account(self):
        name = self.chrome_webdriver.find_element(*self.locator.USER_NAME_FIELD)
        name.send_keys(SampleData.name)

        email = self.chrome_webdriver.find_element(*self.locator.EMAIL_FIELD)
        email.send_keys(SampleData.email)

        password = self.chrome_webdriver.find_element(*self.locator.PASSWORD_FIELD)
        password.send_keys(SampleData.password)

        re_password = self.chrome_webdriver.find_element(*self.locator.RE_ENTER_PASSWORD)
        re_password.send_keys(SampleData.password)

        button = self.chrome_webdriver.find_element(*self.locator.BUTTON)
        button.click()