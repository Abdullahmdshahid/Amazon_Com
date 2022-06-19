from pages.base_page import BasePage
from utils.locators import *
from selenium.webdriver.common.keys import Keys


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
        text = self.chrome_webdriver.find_element(*self.locator.PROFILE).text
        return text

    def click_log_out(self):
        button = self.chrome_webdriver.find_element(*self.locator.LOGOUT)
        button.click()

    def select_search_item(self, type_of_item):
        search_dropdown_box = self.find_elements(*self.locator.SEARCH_DROPDOWN_BOX)
        for search_item in search_dropdown_box:
            if search_item.text == type_of_item:
                search_item.click()
                break

    def enter_search_item_name(self, item):
        search_text_box = self.find_element(*self.locator.SEARCH_TEXT_BOX)
        search_text_box.send_keys(item)
        search_text_box.send_keys(Keys.ENTER)

    def click_location_not_change_button(self):
        button = self.find_element(*self.locator.DONT_CHANGE_BUTTON)
        button.click()

    def click_todays_deal_button(self):
        button = self.find_element(*self.locator.TODAYS_DEALS_BUTTON)
        button.click()
