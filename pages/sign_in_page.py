from pages.base_page import BasePage
from utils.locators import *


class SignInPage(BasePage):

    def __init__(self, chrome_webdriver):
        super().__init__(chrome_webdriver)
        self.locator = LoginPageLocator

    def click_continue_button_with_email(self, email):
        email_text_box = self.find_element(*self.locator.EMAIL_FIELD)
        email_text_box.send_keys(email)
        button = self.find_element(*self.locator.EMAIL_PAGE_BUTTON)
        button.click()

    def click_continue_button_with_password(self, password):
        password_text_box = self.find_element(*self.locator.PASSWORD_FIELD)
        password_text_box.send_keys(password)
        button = self.find_element(*self.locator.LOGIN)
        button.click()

    def get_approve_text(self):
        super().wait_element(*self.locator.APPROVE_TEXT)
        text = self.find_element(*self.locator.APPROVE_TEXT).text
        return text

    def click_create_new_account_button(self):
        button = self.find_element(*self.locator.CREATE_NEW_ACCOUNT)
        button.click()