from pages.base_page import BasePage
from utils.locators import *
from selenium.webdriver.common.keys import Keys


class SearchPage(BasePage):
    def __init__(self, chrome_webdriver):
        self.chrome_webdriver = chrome_webdriver
        super().__init__(chrome_webdriver)
        self.locator = SearchPageLocators

    def search_item_and_select_lowest_price_item(self):
        price_list = []
        # collecting all price
        all_price_list = self.find_elements(*self.locator.ALL_PRICE_LIST)
        # remove unnecessary string and convert string to integer and store those integer value in a list
        for price in all_price_list:
            pr = price.text
            d = pr.replace(",", "")
            price_list.append(int(d))
        price_list.sort()
        # find out the lowest price
        for j in all_price_list:
            e = j.text
            f = e.replace(",", "")

            if int(f) == price_list[0]:
                j.click()
                break