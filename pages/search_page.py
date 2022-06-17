import time

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

    def search_item_with_min_max_price(self, brand_name, min_price, max_price):
        review = self.find_element(*self.locator.FOUR_STAR_REVIEW_BUTTON)
        review.click()
        # time.sleep(3)
        # featured_brands_check_box_text = self.find_elements(*self.locator.FEATURED_BRANDS_TEXT)
        # for brand in featured_brands_check_box_text:
        #     if brand.text == brand_name:
        #         featured_brands_check_box = self.find_element(*self.locator.FEATURED_BRANDS_CHECK_BOX)
        #         featured_brands_check_box.click()
        # time.sleep(3)
        # self.chrome_webdriver.refresh()
        super().scroll_down_by_element(*self.locator.MIN_PRICE_TEXT_BOX)
        min_price_text_box = self.find_element(*self.locator.MIN_PRICE_TEXT_BOX)
        min_price_text_box.send_keys(min_price)
        max_price_text_box = self.find_element(*self.locator.MAX_PRICE_TEXT_BOX)
        max_price_text_box.send_keys(max_price)
        button = self.find_element(*self.locator.GO_BUTTON)
        button.click()
