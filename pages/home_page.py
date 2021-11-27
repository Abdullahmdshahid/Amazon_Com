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
