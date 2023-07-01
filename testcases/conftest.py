from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        chromeoption = webdriver.ChromeOptions()
        chromeoption.binary_location = r'C:\Users\Dell\AppData\Local\Google\Chrome\Application\chrome.exe'
        path = r'C:\Users\Dell\AppData\Local\Programs\Python\Python310\chromedriver.exe'
        service = Service(path)
        service.start()
        driver = webdriver.Chrome(options=chromeoption, service=service)
        return driver
    else:
        driver = webdriver.Firefox()
        return driver




@pytest.fixture()
def pytest_addoption(parser):
    parser.addoption('--browser')


def browser(request):
      return request.config.getoption('--browser')