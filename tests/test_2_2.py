from  tests.base_test import BaseTestClass
from pages.home_page import HomePage
from pages.sign_in_page import SignInPage
from files.sample_data import LoginData


class Test(BaseTestClass):
    def test_tc_2_2(self):
        home_page = HomePage(self.chrome_webdriver)
        home_page.click_login_button()

        sin_in_page = SignInPage(self.chrome_webdriver)
        sin_in_page.click_continue_button_with_email(LoginData.EMAIL)
        sin_in_page.click_continue_button_with_password(LoginData.PASSWORD)
        assert "approve" in sin_in_page.get_approve_text()