from selenium.webdriver import Keys

from pages.base_page import BasePage
from files.sample_data import SampleData
from utils.locators import *


class SignInPage(BasePage):

    def __init__(self, chrome_webdriver):
        super().__init__(chrome_webdriver)
        self.locator = LoginPageLocator

    def click_create_new_account_button(self):
        button = self.chrome_webdriver.find_element(*self.locator.CREATE_NEW_ACCOUNT)
        button.click()