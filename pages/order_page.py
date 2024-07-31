import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderLocators


class OrderPage(BasePage):

    @allure.step('Подготовка к тесту. Убираем со страницы баннер про куки и нажимаем кнопку "Заказать"')
    def prepare_order(self):
        self.dem_cookies()
        self.click_on_element(OrderLocators.ORDER_BUTTON_TOP)

    @allure.step('Заполняем первую страницу формы "Заказать"')
    def fill_fields_to_order_1(self, fields):
        self.set_text_to_element(OrderLocators.NAME, fields['NAME'])
        self.set_text_to_element(OrderLocators.SURNAME, fields['SURNAME'])
        self.set_text_to_element(OrderLocators.ADRES, fields['ADRES'])
        self.click_on_element(OrderLocators.METRO)
        self.set_text_to_element(OrderLocators.METRO, fields['METRO'])
        self.click_on_element(self.format_locator(OrderLocators.STATIONS, fields['METRO']))
        self.set_text_to_element(OrderLocators.TELEPHONE, fields['TELEPHONE'])

    @allure.step('Нажимаем кнопку "Далее"')
    def click_next(self):
        self.click_on_element(OrderLocators.NEXT_BUTTON)

    @allure.step('Заполняем вторую страницу формы "Заказать"')
    def fill_fields_to_order_2(self, fields):
        self.click_on_element(OrderLocators.WHEN)
        self.click_on_element(OrderLocators.CALENDAR_TODAY)
        self.click_on_element(OrderLocators.FOR_HOW_LONG)
        self.click_on_element(self.format_locator(OrderLocators.FOR_HOW_LONG_1, fields['HOWLONG_TEXT']))
        if fields['COLOUR']:
            self.click_on_element(self.format_locator(OrderLocators.COLOUR, fields['COLOUR']))
        if fields['COMMENT']:
            self.set_text_to_element(OrderLocators.COMMENT, fields['COMMENT'])

    @allure.step('Нажимаем кнопку "Заказать"')
    def click_order(self):
        self.click_on_element(OrderLocators.ORDER_BUTTON_BOTTOM)

    @allure.step('Нажимаем кнопку "Да"')
    def click_yes(self):
        self.click_on_element(OrderLocators.YES_BUTTON)

    @allure.step('Получаем текст сообщения о сделанном заказе и возвращаем его номер')
    def get_order_num(self):
        str = self.get_text_from_element(OrderLocators.ORDER_NUM)
        n = str[14:str.rfind('.')]
        return n

    @allure.step('Переходим по кнопке "Посмотреть статус заказа"')
    def click_status(self):
        self.click_on_element(OrderLocators.STATUS_BUTTON)
