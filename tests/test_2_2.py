import pytest
from pages.home_page import HomePage
from pages.sign_in_page import SignInPage


@pytest.mark.usefixtures("main")
class Test(object):
    def test_tc_2_2(self):
        home_page = HomePage(self.chrome_webdriver)
        home_page.click_login_button()

        sin_in_page = SignInPage(self.chrome_webdriver)
        sin_in_page.click_continue_button_with_email()
        sin_in_page.click_continue_button_with_password()
        home_page.hover_profile()
        # user_name = home_page.get_profile_name()
        # home_page.click_log_out()
        print(home_page.get_profile_name())
        # assert "aaa" == user_name