from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class MainPage:
    # Кнопки «Заказать»
    ORDER_BUTTON_HEADER = (
        By.XPATH,
        "(//button[normalize-space()='Заказать'])[1]"
    )
    ORDER_BUTTON_BOTTOM = (
        By.XPATH,
        "(//button[normalize-space()='Заказать'])[last()]"
    )

    # Логотипы
    LOGO_SCOOTER = (
        By.XPATH,
        "//a[contains(@class, 'LogoScooter')]"
    )
    LOGO_YANDEX = (
        By.XPATH,
        "//a[contains(@class, 'LogoYandex')]"
    )

    # Вопросы и ответы FAQ
    FAQ_QUESTION = (By.ID, "accordion__heading-{0}")
    FAQ_ANSWER = (By.ID, "accordion__panel-{0}")

    def __init__(self, driver):
        self.driver = driver

    def click_order_button_header(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                self.ORDER_BUTTON_HEADER
            )
        ).click()

    def click_order_button_bottom(self):
        # Закрываем баннер cookie, если он появился
        cookie_buttons = self.driver.find_elements(
            By.CSS_SELECTOR,
            "div[class*='App_CookieConsent'] button"
        )

        if cookie_buttons:
            cookie_buttons[0].click()

        # Находим нижнюю кнопку «Заказать»
        order_button = self.driver.find_element(
            *self.ORDER_BUTTON_BOTTOM
        )

        # Прокручиваем страницу к кнопке
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            order_button
        )

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                self.ORDER_BUTTON_BOTTOM
            )
        ).click()

    def click_logo_scooter(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                self.LOGO_SCOOTER
            )
        ).click()

    def click_logo_yandex(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                self.LOGO_YANDEX
            )
        ).click()