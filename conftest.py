import pytest
from selenium import webdriver
from urls import MAIN_URL


@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get(MAIN_URL)

    yield browser

    browser.quit()