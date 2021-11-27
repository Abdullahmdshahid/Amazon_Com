import pytest

from pages.home_page import HomePage


@pytest.mark.usefixtures("main")
class Test(object):
    def test_tc_1(self):
        home_page = HomePage(self.chrome_webdriver)
        url = home_page.chrome_webdriver.current_url
        assert 'https://www.amazon.com/' == url
