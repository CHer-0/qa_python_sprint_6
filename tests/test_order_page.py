import pytest
import allure
from data import FirstScenario
from data import SecondScenario
from locators.order_page_locators import OrderLocators
from links import Urls


class TestOrderPage:

    @allure.title('Проверка 2 сценариев заполнения формы Заказа самоката')
    @pytest.mark.parametrize("data", [FirstScenario, SecondScenario])
    def test_make_order(self, order_page, data):
        order_page.prepare_order()

        order_page.set_text_to_element(OrderLocators.NAME, data.NAME)
        order_page.set_text_to_element(OrderLocators.SURNAME, data.SURNAME)
        order_page.set_text_to_element(OrderLocators.ADRES, data.ADRES)
        order_page.click_on_element(OrderLocators.METRO)
        order_page.set_text_to_element(OrderLocators.METRO, data.METRO)
        order_page.click_on_element(order_page.format_locator(OrderLocators.STATIONS, data.METRO))
        order_page.set_text_to_element(OrderLocators.TELEPHONE, data.TELEPHONE)

        order_page.click_on_element(OrderLocators.NEXT_BUTTON)

        order_page.click_on_element(OrderLocators.WHEN)
        order_page.click_on_element(OrderLocators.CALENDAR_TODAY)
        order_page.click_on_element(OrderLocators.FOR_HOW_LONG)
        order_page.click_on_element(order_page.format_locator(OrderLocators.FOR_HOW_LONG_1, data.HOWLONG_TEXT))
        if data.COLOUR:
            order_page.click_on_element(order_page.format_locator(OrderLocators.COLOUR, data.COLOUR))
        if data.COMMENT:
            order_page.set_text_to_element(OrderLocators.COMMENT, data.COMMENT)
        order_page.click_on_element(OrderLocators.ORDER_BUTTON_BOTTOM)

        order_page.click_on_element(OrderLocators.YES_BUTTON)

        str = order_page.get_text_from_element(OrderLocators.ORDER_NUM)
        str = str[14:str.rfind('.')]

        expected_url = Urls.URL_STATUS + str
        order_page.click_on_element(OrderLocators.STATUS_BUTTON)

        assert order_page.get_url() == expected_url

