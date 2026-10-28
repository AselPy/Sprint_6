from selenium.webdriver.common.by import By


class MainPageLocators:
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

    # Кнопка закрытия баннера cookie
    COOKIE_BUTTON = (
        By.CSS_SELECTOR,
        "div[class*='App_CookieConsent'] button"
    )

    # Заголовок формы заказа
    ORDER_FORM_TITLE = (
        By.XPATH,
        "//*[contains(text(), 'Для кого самокат')]"
    )


class OrderPageLocators:
    # Поля первой формы
    FIRST_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (
        By.XPATH,
        "//input[@placeholder='* Адрес: куда привезти заказ']"
    )
    METRO_STATION = (
        By.XPATH,
        "//input[@placeholder='* Станция метро']"
    )
    PHONE = (
        By.XPATH,
        "//input[@placeholder='* Телефон: на него позвонит курьер']"
    )
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
    CONFIRM_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Да']"
    )

    # Сообщение об успешном оформлении
    ORDER_SUCCESS = (
        By.XPATH,
        "//*[contains(text(), 'Заказ оформлен')]"
    )

    # Динамические локаторы
    METRO_STATION_OPTION = (
        By.XPATH,
        "//button[contains(@class, 'select-search__option') "
        "and normalize-space()='{0}']"
    )
    RENTAL_DAY = (
        By.XPATH,
        "//div[contains(@class, 'react-datepicker__day') "
        "and normalize-space()='{0}' "
        "and not(contains(@class, "
        "'react-datepicker__day--outside-month'))]"
    )
    RENTAL_PERIOD_OPTION = (
        By.XPATH,
        "//div[contains(@class, 'Dropdown-option') "
        "and normalize-space()='{0}']"
    )