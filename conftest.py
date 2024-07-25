import pytest
from selenium import webdriver
from links import Urls
from pages.main_page import MainPage
from pages.order_page import OrderPage


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture()
def main_page(driver):
    page = MainPage(driver)
    page.driver.get(Urls.URL_MAIN)
    return page


@pytest.fixture()
def order_page(driver):
    page = OrderPage(driver)
    page.driver.get(Urls.URL_ORDER)
    return page


@pytest.fixture()
def test_status_page(driver):
    page = MainPage(driver)
    page.driver.get(Urls.URL_STATUS_TEST)
    return page
