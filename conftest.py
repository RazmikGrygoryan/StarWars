import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.lightsabers_page import LightSabers
from pages.accessories_page import Accessories
from pages.handle_pages import Handle
from pages.items_page import Items


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    chrome_driver = webdriver.Chrome(options=options)
    return chrome_driver


@pytest.fixture()
def light_sabers_page(driver):
    return LightSabers(driver)


@pytest.fixture()
def accessories_page(driver):
    return Accessories(driver)


@pytest.fixture()
def handle_page(driver):
    return Handle(driver)


@pytest.fixture()
def items_page(driver):
    return Items(driver)