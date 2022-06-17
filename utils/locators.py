from selenium.webdriver.common.by import By


class HomePageLocator(object):
    # SIGN IN BUTTON

    SIGN_IN_BUTTON = (By.XPATH, '//a[@id="nav-link-accountList"]')

    # FACEBOOK BUTTON

    PROFILE = (By.XPATH, '//span[@id="nav-link-accountList-nav-line-1"]')

    # GOOGLE BUTTON

    GOOGLE_BUTTON = (By.XPATH, '//*[@id="js--login-form"]/div[1]/div/button[2]')

    # SIGN UP BUTTON

    SIGN_UP_BUTTON = (By.XPATH, '//p[text()="Sign up"]')

    # SIGN UP BY FACEBOOK

    SIGN_IN_FB = (By.XPATH, '//*[@id="js--registration-form"]/div[1]/div/button[1]')

    # SIGN UP GOOGLE

    SIGN_IN_GOOGLE = (By.XPATH, '//*[@id="js--registration-form"]/div[1]/div/button[2]')

    # FIRST NAME

    NAME = (By.ID, "nm")

    # EMAIL

    EMAIL = (By.ID, "js-email")

    # PHONE

    PHONE = (By.ID, "js-phone")

    # CREATE PASSWORD

    CREATE_PASSWORD = (By.ID, "pwd")

    # PROFILE = (By.XPATH, '//span[@class="user-name"]')
    ACCOUNT = (By.XPATH, '//a[@id="nav-link-accountList"]')

    TODAYS_DEALS_BUTTON = (By.XPATH, '//div[@id="nav-xshop"]/a[1]')
    ELEC_BUTTON = (By.XPATH, '//a[@href="/electronics?ref=nm"]')
    STAI_BUTTON = (By.XPATH, '//a[@href="/stationary?ref=nm"]')
    GIFT_BUTTON = (By.XPATH, '//a[@href="/giftfinder?ref=nm"]')
    CORPO_BUTTON = (By.XPATH, '//a[@href="/corporate?ref=nm"]')
    OFFER_BUTTON = (By.XPATH, '//a[@href="/offer?ref=nm"]')
    BLOG_BUTTON = (By.XPATH, '//a[@href="https://blog.rokomari.com/?ref=nm"]')
    CHART_BUTTON = (By.XPATH, '//a[@class="cart-menu"]')
    NOTIFY_BUTTON = (By.XPATH, 'a[class*="notify"]')
    SEARCH_DROPDOWN_BOX = (By.CSS_SELECTOR, 'select[class*="search-dropdown"] option')
    SEARCH_TEXT_BOX = (By.ID, 'twotabsearchtextbox')
    ORDER = (By.XPATH, '//a[text()="My Orders"]')
    MY_LIST = (By.XPATH, '//a[text()="My List"]')
    CREATE_LIST = (By.XPATH, '//button[text()="Create New List"]')
    WISH_LIST = (By.XPATH, '//a[text()="My Wishlist"]')
    REVIEWS = (By.XPATH, '//a[text()="My Rating Reviews"]')
    POINT = (By.XPATH, '//a[text()="My Points"]')
    LOGOUT = (By.XPATH, '//span[text()="Sign Out"]')


class LoginPageLocator(object):
    # LOGIN EMAIL FIELD

    EMAIL_FIELD = (By.XPATH, '//input[@id="ap_email"]')

    # EMAIL PAGE BUTTON

    EMAIL_PAGE_BUTTON = (By.XPATH, '//input[@id="continue"]')

    # LOGIN PASSWORD FIELD

    PASSWORD_FIELD = (By.XPATH, '//input[@id="ap_password"]')

    # LOGIN BUTTON

    LOGIN = (By.XPATH, '//*[@id="signInSubmit"]')

    CREATE_NEW_ACCOUNT = (By.XPATH, '//a[@id="createAccountSubmit"]')
    APPROVE_TEXT = (By.XPATH, '//div[@class="a-box-inner"]/div[2]/span')


class ChangeProfileLocator(object):
    CHANGE_PROFILE = (By.ID, 'js--edit-personal')

    CHANGE_NAME = (By.XPATH, '//input[@name="name"]')

    BIRTH_DATE = (By.XPATH, '//input[@name="dob"]')

    MALE_BUTTON = (By.XPATH, '//input[@name="customRadioInline1"]')

    CHANGE_SAVE = (By.XPATH, '//input[@id="personalInfo"]')


class RegisterPageLocator(object):
    USER_NAME_FIELD = (By.XPATH, '//input[@id="ap_customer_name"]')

    EMAIL_FIELD = (By.XPATH, '//input[@id="ap_email"]')

    PASSWORD_FIELD = (By.XPATH, '//input[@id="ap_password"]')

    RE_ENTER_PASSWORD = (By.XPATH, '//input[@id="ap_password_check"]')

    BUTTON = (By.XPATH, '//input[@id="continue"]')


class LocationAlertBoxLocator(object):
    DONT_CHANGE_BUTTON = (By.XPATH, '//*[@id="nav-main"]/div[1]/div/div/div[3]/span[1]/span/input')


class SearchPageLocators(object):
    ALL_PRICE_LIST = (By.XPATH, '//span[contains(text(),"$")]/parent::span[@aria-hidden="true"]/span[2]')
    FOUR_STAR_REVIEW_BUTTON = (By.XPATH, '//li[@id="p_72/1248879011"]/span/a')
    FEATURED_BRANDS_TEXT = (By.XPATH, '//ul[@aria-labelledby="p_89-title"]/li/span/a/span')
    FEATURED_BRANDS_CHECK_BOX = (By.XPATH, '//ul[@aria-labelledby="p_89-title"]/li/span/a')
    MIN_PRICE_TEXT_BOX = (By.ID, "low-price")
    MAX_PRICE_TEXT_BOX = (By.ID, "high-price")
    GO_BUTTON = (By.XPATH, '//span[contains(text(), "Go")]/parent::span/input')