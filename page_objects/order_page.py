from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class OrderPage:
    # Поля первой формы
    FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Поля второй формы
    RENTAL_DATE = (
        By.XPATH,
        "//input[@placeholder='* Когда привезти самокат']"
    )
    RENTAL_PERIOD = (By.CLASS_NAME, "Dropdown-control")
    RENTAL_COMMENT = (
        By.XPATH,
        "//input[@placeholder='Комментарий для курьера']"
    )

    # Цвет самоката
    BLACK_COLOR = (By.ID, "black")
    GREY_COLOR = (By.ID, "grey")

    # Кнопки заказа
    ORDER_BUTTON = (
        By.XPATH,
        "(//button[normalize-space()='Заказать'])[last()]"
    )
    CONFIRM_BUTTON = (By.XPATH, "//button[normalize-space()='Да']")

    # Сообщение об успешном оформлении
    ORDER_SUCCESS = (
        By.XPATH,
        "//*[contains(text(), 'Заказ оформлен')]"
    )

    def __init__(self, driver):
        self.driver = driver

    def fill_personal_data(
        self, first_name, last_name, address, metro_station, phone
    ):
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.ADDRESS).send_keys(address)

        metro = self.driver.find_element(*self.METRO_STATION)
        metro.click()
        metro.send_keys(metro_station)

        station_locator = (
            By.XPATH,
            "//button[contains(@class, 'select-search__option') "
            f"and normalize-space()='{metro_station}']"
        )

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(station_locator)
        ).click()

        self.driver.find_element(*self.PHONE).send_keys(phone)

    def click_next_button(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.NEXT_BUTTON)
        ).click()

    def fill_rental_data(self, rental_date, rental_period, color, comment):
        # Открываем календарь
        date_field = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.RENTAL_DATE)
        )
        date_field.click()

        # Выбираем день в календаре
        day = int(rental_date.split('.')[0])

        day_locator = (
            By.XPATH,
            "//div[contains(@class, 'react-datepicker__day') "
            f"and normalize-space()='{day}' "
            "and not(contains(@class, "
            "'react-datepicker__day--outside-month'))]"
        )

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(day_locator)
        ).click()

        # Открываем список срока аренды
        period = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.RENTAL_PERIOD)
        )
        period.click()

        # Находим и выбираем нужный срок
        period_locator = (
            By.XPATH,
            "//div[contains(@class, 'Dropdown-option') "
            f"and normalize-space()='{rental_period}']"
        )

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(period_locator)
        ).click()

        # Выбираем цвет самоката
        if color == 'black':
            self.driver.find_element(*self.BLACK_COLOR).click()
        else:
            self.driver.find_element(*self.GREY_COLOR).click()

        # Заполняем комментарий
        self.driver.find_element(*self.RENTAL_COMMENT).send_keys(comment)

    def click_order_button(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.ORDER_BUTTON)
        ).click()

    def confirm_order(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.CONFIRM_BUTTON)
        ).click()

    def wait_for_successful_order(self):
        return WebDriverWait(self.driver, 15).until(
            expected_conditions.visibility_of_element_located(
                self.ORDER_SUCCESS
            )
        )