from pages.base_page import BasePage
from locators.main_page_locators import MainLocators


class MainPage(BasePage):

    def prepare_main(self):
        self.dem_cookies(),
        self.scrolldown()

    def get_text_any_answer(self, n):
        locator_q = self.format_locator(MainLocators.QUESTIONS, n)
        locator_a = self.format_locator(MainLocators.ANSWERS, n)
        self.click_on_element(locator_q)
        return self.get_text_from_element(locator_a)

    @allure.title('Проверка соответствия 8 вопросов и ответов на них на главной форме')
    def click_samokat(self):
        self.click_on_element(MainLocators.SAMOKAT_BUTTON)

    def click_yandex(self):
        self.click_on_element(MainLocators.YANDEX_BUTTON)

    def wait_yandex(self):
        self.find_element_and_wait(MainLocators.YANDEX_ELEMENT)

