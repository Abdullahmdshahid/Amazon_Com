from pages.base_page import BasePage
from utils.locators import *


class LocationAlertPage(BasePage):

    def __init__(self, chrome_webdriver):
        super().__init__(chrome_webdriver)
        self.locator = LocationAlertBoxLocator

    def click_dont_change_button(self):
        button = self.chrome_webdriver.find_element(*self.locator.DONT_CHANGE_BUTTON)
        button.click()