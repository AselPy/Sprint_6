import pytest
from selenium import webdriver
from urls import MAIN_URL
from page_objects.main_page import MainPage


@pytest.fixture
def driver():
    browser = webdriver.Firefox()
    main_page = MainPage(browser)

    main_page.maximize_window()
    main_page.open_page(MAIN_URL)

    yield browser

    main_page.quit_browser()
