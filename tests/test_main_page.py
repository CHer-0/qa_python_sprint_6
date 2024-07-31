import allure
import pytest
from data import Accordeon
from data import OrderButtons
from links import Urls


# класс с автотестом
class TestMainPage:

    @allure.title('Проверка соответствия 8 вопросов и ответов на них на главной форме')
    @allure.link('https://qa-scooter.praktikum-services.ru/', name='Тестируемый сайт')
    @pytest.mark.parametrize("qa", Accordeon.answers_questions)
    def test_questions(self, main_page, qa):
        main_page.prepare_main()
        n, expected_answer = qa
        result = main_page.get_text_any_answer(n)
        assert result == expected_answer

    @allure.title('Проверка перехода с главной формы по 2 кнопкам "Заказать"')
    @pytest.mark.parametrize("button", OrderButtons.buttons)
    def test_order_buttons(self, main_page, button):
        main_page.dem_cookies()
        main_page.click_on_element(button)
        assert main_page.get_url() == Urls.URL_ORDER

    @allure.title('Проверка перехода с формы проверки статуса тестового заказа на главную форму по кнопке "Самокат"')
    def test_samokat_button(self, test_status_page):
        test_status_page.click_samokat()
        assert test_status_page.get_url() == Urls.URL_MAIN

    @allure.title('Проверка перехода с главной формы по кнопке "Яндекс"')
    def test_yandex_button(self, main_page):
        main_page.click_yandex()
        main_page.switch_to_new_window()
        main_page.wait_yandex()
        assert main_page.get_url() == Urls.URL_YANDEX
