import allure
import pytest
from data import ORDER_DATA
from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage


class TestOrder:

    @allure.title('Оформление заказа: {first_name} {last_name}')
    @pytest.mark.parametrize(
        'first_name, last_name, address, metro_station, phone, '
        'rental_date, rental_period, color, comment',
        ORDER_DATA
    )
    def test_create_order(
        self, driver, first_name, last_name, address,
        metro_station, phone, rental_date, rental_period,
        color, comment
    ):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        # Открываем форму заказа
        main_page.click_order_button_header()

        # Заполняем данные заказчика
        order_page.fill_personal_data(
            first_name, last_name, address, metro_station, phone
        )
        order_page.click_next_button()

        # Заполняем данные аренды
        order_page.fill_rental_data(
            rental_date, rental_period, color, comment
        )

        # Оформляем заказ
        order_page.click_order_button()
        order_page.confirm_order()

        # Проверяем успешное оформление
        success_message = order_page.wait_for_successful_order()

        assert 'Заказ оформлен' in success_message.text
