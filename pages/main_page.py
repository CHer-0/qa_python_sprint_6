import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainLocators


class MainPage(BasePage):

    @allure.step('Подготовка к тесту. Убираем со страницы баннер про куки и прокручиваем страницу до-низу')
    def prepare_main(self):
        self.dem_cookies(),
        self.scrolldown()

    @allure.step('для каждого вопроса и соответствующего ему ответа получаем локаторы и возврашаем текст ответа')
    def get_text_any_answer(self, n):
        locator_q = self.format_locator(MainLocators.QUESTIONS, n)
        locator_a = self.format_locator(MainLocators.ANSWERS, n)
        self.click_on_element(locator_q)
        return self.get_text_from_element(locator_a)

    @allure.step('Нажимаем кнопку "Самокат" в верхнем левом углу гдавной страницы')
    def click_samokat(self):
        self.click_on_element(MainLocators.SAMOKAT_BUTTON)

    @allure.step('Нажимаем кнопку "Яндекс" в верхнем левом углу гдавной страницы')
    def click_yandex(self):
        self.click_on_element(MainLocators.YANDEX_BUTTON)

    @allure.step('Ожидаем загрузки Дзена')
    def wait_yandex(self):
        self.find_element_and_wait(MainLocators.YANDEX_ELEMENT)

