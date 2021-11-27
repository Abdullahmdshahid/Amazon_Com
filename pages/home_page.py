from selenium.webdriver import Keys

from pages.base_page import BasePage
from files.sample_data import SampleData
from utils.locators import *


class HomePage(BasePage):

    def __init__(self, chrome_webdriver):
        super().__init__(chrome_webdriver)
        self.locator = HomePageLocator

    def click_login_button(self):
        button = self.chrome_webdriver.find_element(*self.locator.SIGN_IN_BUTTON)
        button.click()

    def hover_profile(self):
        super().hover(*self.locator.ACCOUNT)

    def get_profile_name(self):
        super().wait_element(*self.locator.PROFILE)
        button = self.chrome_webdriver.find_element(*self.locator.PROFILE).text

    def click_log_out(self):
        button = self.chrome_webdriver.find_element(*self.locator.LOGOUT)
        button.click()