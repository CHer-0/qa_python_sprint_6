from pages.base_page import BasePage
from locators.order_page_locators import OrderLocators


class OrderPage(BasePage):

    def prepare_order(self):
        self.dem_cookies()
        self.click_on_element(OrderLocators.ORDER_BUTTON_TOP)