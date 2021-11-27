import pytest
from pages.home_page import HomePage
from pages.sign_in_page import SignInPage


@pytest.mark.usefixtures("main")
class Test(object):
    def test_tc_2_3(self):
        home_page = HomePage(self.chrome_webdriver)
        home_page.click_login_button()

        sin_in_page = SignInPage(self.chrome_webdriver)
        sin_in_page.click_continue_button_with_email()
        sin_in_page.click_continue_button_with_password()
        home_page.hover_profile()
        home_page.click_log_out()