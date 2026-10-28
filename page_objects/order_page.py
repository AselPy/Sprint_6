import allure
from page_objects.base_page import BasePage
from locators.locators import OrderPageLocators


class OrderPage(BasePage):

    @allure.step('Заполнить личные данные')
    def fill_personal_data(
        self, first_name, last_name, address, metro_station, phone
    ):
        self.send_keys_to_element(
            OrderPageLocators.FIRST_NAME, first_name
        )
        self.send_keys_to_element(
            OrderPageLocators.LAST_NAME, last_name
        )
        self.send_keys_to_element(
            OrderPageLocators.ADDRESS, address
        )

        self.click_element(OrderPageLocators.METRO_STATION)
        self.send_keys_to_element(
            OrderPageLocators.METRO_STATION, metro_station
        )

        station_locator = (
            OrderPageLocators.METRO_STATION_OPTION[0],
            OrderPageLocators.METRO_STATION_OPTION[1].format(
                metro_station
            )
        )
        self.click_element(station_locator)

        self.send_keys_to_element(
            OrderPageLocators.PHONE, phone
        )

    @allure.step('Нажать кнопку «Далее»')
    def click_next_button(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполнить данные аренды')
    def fill_rental_data(
        self, rental_date, rental_period, color, comment
    ):
        self.click_element(OrderPageLocators.RENTAL_DATE)

        day = int(rental_date.split('.')[0])

        day_locator = (
            OrderPageLocators.RENTAL_DAY[0],
            OrderPageLocators.RENTAL_DAY[1].format(day)
        )
        self.click_element(day_locator)

        self.click_element(OrderPageLocators.RENTAL_PERIOD)

        period_locator = (
            OrderPageLocators.RENTAL_PERIOD_OPTION[0],
            OrderPageLocators.RENTAL_PERIOD_OPTION[1].format(
                rental_period
            )
        )
        self.click_element(period_locator)

        if color == 'black':
            self.click_element(OrderPageLocators.BLACK_COLOR)
        else:
            self.click_element(OrderPageLocators.GREY_COLOR)

        self.send_keys_to_element(
            OrderPageLocators.RENTAL_COMMENT, comment
        )

    @allure.step('Нажать кнопку «Заказать»')
    def click_order_button(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Подтвердить оформление заказа')
    def confirm_order(self):
        self.click_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step('Дождаться успешного оформления заказа')
    def wait_for_successful_order(self):
        return self.wait_for_element(
            OrderPageLocators.ORDER_SUCCESS
        )