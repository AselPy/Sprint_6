import pytest
from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage


class TestOrder:

    @pytest.mark.parametrize(
        'first_name, last_name, address, metro_station, phone, '
        'rental_date, rental_period, color, comment',
        [
            (
                'Самат',
                'Осмонов',
                'Кыргызстан, Бишкек, проспект Чуй, 123',
                'Черкизовская',
                '89995551234',
                '30.10.2026',
                'сутки',
                'black',
                'Позвонить перед доставкой'
            ),
            (
                'Айгул',
                'Абдраимова',
                'Кыргызстан, Бишкек, улица Манаса, 45',
                'Сокольники',
                '89995554321',
                '31.10.2026',
                'двое суток',
                'grey',
                'Доставить вечером'
            )
        ]
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