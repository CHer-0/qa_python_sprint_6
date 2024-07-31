from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from locators.main_page_locators import MainLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def setup(self):
        options = Options()
        options.add_argument('--window-size=1920,1080')
        service = Service()
        self.driver = webdriver.Firefox(service=service, options=options)

    def find_element_and_wait(self, locator):
        WebDriverWait(self.driver, 7).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def find_element_wait(self, locator):
        WebDriverWait(self.driver, 7).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        self.find_element_wait(locator).click()

    def get_text_from_element(self, locator):
        elt = self.find_element_and_wait(locator)
        return elt.text

    def set_text_to_element(self, locator, text):
        elt = self.find_element_and_wait(locator)
        elt.send_keys(text)


    @staticmethod
    def format_locator(locator, n):
        method, locator1 = locator
        locator2 = locator1.format(n)
        return method, locator2

    def dem_cookies(self):
        try:
            but = self.driver.find_element(*MainLocators.COOKIE_BUTTON)
            but.click()
        except Exception:
            pass

    def scrolldown(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def get_url(self):
        return self.driver.current_url

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def teardown(self):
        self.driver.close()
