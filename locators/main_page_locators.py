from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class MainLocators:

    # локатор кнопки «Заказать» сверху
    ORDER_BUTTON_TOP = [By.XPATH, './/button[@class="Button_Button__ra12g"]']
    # локатор кнопки «Заказать» внизу
    ORDER_BUTTON_BOTTOM = [By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM"]']
    # локатор кнопки «Да все привыкли» внизу в приглашении использовать куки
    COOKIE_BUTTON = [By.ID, 'rcc-confirm-button']
    # общий локатор вопросов
    QUESTIONS = [By.ID, 'accordion__heading-{}']
    # общий локатор ответов
    ANSWERS = [By.XPATH, ".//div[@aria-labelledby='accordion__heading-{}']/p"]
    # локатор кнопки «Самокат» вверху слева
    SAMOKAT_BUTTON = [By.XPATH, './/img[@alt="Scooter"]']
    # локатор кнопки «Яндекс» вверху слева
    YANDEX_BUTTON = [By.XPATH, './/img[@alt="Yandex"]']

    YANDEX_ELEMENT = [By.ID, 'SECOND_CHUNK_APP_CONTAINER_MicroRoot']
