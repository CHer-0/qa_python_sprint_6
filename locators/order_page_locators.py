from selenium.webdriver.common.by import By


class OrderLocators:
    # Поле Имя
    NAME = [By.XPATH, './/input[@placeholder="* Имя"]']
    # Поле Фамилия
    SURNAME = [By.XPATH, './/input[@placeholder="* Фамилия"]']
    # Поле Адрес
    ADRES = [By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]']
    # Поле Станция метро
    METRO = [By.XPATH, './/input[@placeholder="* Станция метро"]']
    # Выбор Станции метро из списка
    STATIONS = [By.XPATH, './/div[text()="{}"]']
    # Поле Телефон
    TELEPHONE = [By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]']
    # Кнопка Далее
    NEXT_BUTTON = [By.XPATH, './/button[text()="Далее"]']
    # Кнопка САМОКАТ наверху слева
    SAMOKAT_BUTTON = [By.XPATH, './/img[@alt="Scooter"]']
    # Кнопка Яндекс наверху слева
    YANDEX_BUTTON = [By.XPATH, './/img[@alt="Yandex"]']
    # Дата доставки
    WHEN = [By.XPATH, './/input[@placeholder="* Когда привезти самокат"]']
    # Календарик
    CALENDAR = [By.XPATH, './/div[@class="react-datepicker-popper"]']
    # Сегодня
    CALENDAR_TODAY = [By.XPATH, './/div[@tabindex="0" and @role="button"]']
    # На сколько суток
    FOR_HOW_LONG = [By.XPATH, './/div[@class="Dropdown-control"]']
    # 1 - 7 суток
    FOR_HOW_LONG_1 = [By.XPATH, './/div[text()="{}"]']

    # "Цвет самоката"
    COLOUR = [By.ID, '{}']
    # Комментарий для курьера
    COMMENT = [By.XPATH, './/input[@placeholder="Комментарий для курьера"]']
    # Кнопка Назад
    BACK_BUTTON = [By.XPATH, './/button[text()="Назад"]']
    # локатор кнопки «Заказать» сверху
    ORDER_BUTTON_TOP = [By.XPATH, './/button[@class="Button_Button__ra12g"]']
    # локатор кнопки «Заказать» внизу
    ORDER_BUTTON_BOTTOM = [By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM"]']
    # локатор кнопки «Да»
    YES_BUTTON = [By.XPATH, './/button[text()="Да"]']
    # локатор кнопки «Посмотреть статус»
    STATUS_BUTTON = [By.XPATH, './/button[text()="Посмотреть статус"]']
    # локатор с текстом номера заказа
    ORDER_NUM = [By.XPATH, './/div[@class="Order_Text__2broi"]']
