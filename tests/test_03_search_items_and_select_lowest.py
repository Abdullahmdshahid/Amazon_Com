from tests.base_test import BaseTestClass
from pages.home_page import HomePage
from pages.search_page import SearchPage
from files.sample_data import SearchData


class Test(BaseTestClass):
    def test_03(self):
        home_page = HomePage(chrome_webdriver=self.chrome_webdriver)
        home_page.select_search_item(SearchData.TYPE_OF_ITEM)
        home_page.enter_search_item_name(SearchData.ITEM_NAME)
        search_page = SearchPage(chrome_webdriver=self.chrome_webdriver)
        search_page.search_item_and_select_lowest_price_item()