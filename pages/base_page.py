from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# this Base class is serving basic attributes for every single page inherited from Page class

class BasePage(object):

    def __init__(self, chrome_webdriver):
        self.chrome_webdriver = chrome_webdriver
        self.timeout = 30

    def find_element(self, *locator):
        return self.chrome_webdriver.find_element(*locator)

    def find_elements(self, *locator):
        return self.chrome_webdriver.find_elements(*locator)

    def get_title(self):
        return self.chrome_webdriver.title

    def get_url(self):
        return self.chrome_webdriver.current_url

    def back_to_homepage(self):
        return self.chrome_webdriver.back()

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.chrome_webdriver).move_to_element(element)
        hover.perform()

    def wait_element(self, *locator):
        try:
            WebDriverWait(self.chrome_webdriver, 10).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print("\n * ELEMENT NOT FOUND WITHIN GIVEN TIME! --> %s" % (locator[1]))
            self.chrome_webdriver.quit()

    def scroll_down(self):
        self.chrome_webdriver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def scroll_up(self):
        self.chrome_webdriver.execute_script("window.scrollTo(0,0)")

    def scroll_down_by_pixel(self):
        self.chrome_webdriver.execute_script("window.scrollBy(0,1000)")

    def scroll_down_by_element(self, *locator):
        element = self.chrome_webdriver.find_element(*locator)
        self.chrome_webdriver.execute_script("arguments[0].scrollIntoView();", element)

