import pytest
import allure
from links import Urls
from data import FirstScenario
from data import SecondScenario


class TestOrderPage:

    @allure.title('Проверка 2 сценариев заполнения формы Заказа самоката')
    @pytest.mark.parametrize("data", [FirstScenario.FIELDS, SecondScenario.FIELDS])
    def test_make_order(self, order_page, data):
        order_page.prepare_order()
        order_page.fill_fields_to_order_1(data)
        order_page.click_next()
        order_page.fill_fields_to_order_2(data)
        order_page.click_order()
        order_page.click_yes()
        expected_url = Urls.URL_STATUS + order_page.get_order_num()
        order_page.click_status()
        assert order_page.get_url() == expected_url

