import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

@pytest.fixture(scope='class')
def main(request):
    chrome_service = Service(os.getcwd() + r"\browser\chromedriver.exe")
    chrome_webdriver = webdriver.Chrome(service=chrome_service)
    chrome_webdriver.get("https://www.amazon.com/")
    chrome_webdriver.maximize_window()
    request.cls.chrome_webdriver = chrome_webdriver

    yield
    chrome_webdriver.close()