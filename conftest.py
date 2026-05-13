import pytest

from utils.driver_factory import DriverFactory
from pages.LoginPage import LoginPage


@pytest.fixture
def driver():

    factory = DriverFactory("chrome")   #create object
    driver = factory.get_driver()       # get browser

    yield driver

    driver.quit()                       #close browser

@pytest.fixture
def login_page(driver):
    page = LoginPage(driver)
    page.open()

    return page





