import pytest
from selenium import webdriver
from urls import MAIN_URL
from page_objects.base_page import BasePage


@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    base_page = BasePage(browser)

    base_page.maximize_window()
    base_page.open_page(MAIN_URL)

    yield browser

    base_page.quit_browser()