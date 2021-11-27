from selenium.webdriver import Keys

from pages.base_page import BasePage
from files.sample_data import SampleData
from utils.locators import *


class SignInPage(BasePage):

    def __init__(self, chrome_webdriver):
        super().__init__(chrome_webdriver)
        self.locator = LoginPageLocator

    def click_continue_button_with_email(self):
        email = self.chrome_webdriver.find_element(*self.locator.EMAIL_FIELD)
        email.send_keys(SampleData.email)
        button = self.chrome_webdriver.find_element(*self.locator.EMAIL_PAGE_BUTTON)
        button.click()

    def click_continue_button_with_password(self):
        password = self.chrome_webdriver.find_element(*self.locator.PASSWORD_FIELD)
        password.send_keys(SampleData.password)
        button = self.chrome_webdriver.find_element(*self.locator.LOGIN)
        button.click()

    def click_create_new_account_button(self):
        button = self.chrome_webdriver.find_element(*self.locator.CREATE_NEW_ACCOUNT)
        button.click()