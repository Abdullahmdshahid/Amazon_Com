import pytest
from pages.home_page import HomePage
from pages.sign_in_page import SignInPage
from pages.register_page import RegisterPage


@pytest.mark.usefixtures("main")
class Test(object):
    def test_tc_2_1(self):
        home_page = HomePage(self.chrome_webdriver)
        home_page.click_login_button()

        sin_in_page = SignInPage(self.chrome_webdriver)
        sin_in_page.click_create_new_account_button()

        register_page = RegisterPage(self.chrome_webdriver)
        register_page.create_new_account()
        # url = home_page.chrome_webdriver.current_url
        # assert 'https://www.amazon.com/' == url