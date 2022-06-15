from tests.base_test import BaseTestClass
from pages.home_page import HomePage


class Test(BaseTestClass):
    def test_tc_1(self):
        home_page = HomePage(self.chrome_webdriver)
        assert 'https://www.amazon.com/' == home_page.get_url()
