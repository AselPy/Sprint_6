import allure
from page_objects.main_page import MainPage
from urls import MAIN_URL


class TestNavigation:

    @allure.title('Проверка открытия формы заказа по нижней кнопке')
    def test_order_button_bottom_opens_form(self, driver):
        main_page = MainPage(driver)

        main_page.click_order_button_bottom()

        assert main_page.is_order_form_visible()

    @allure.title('Проверка перехода на главную страницу по логотипу Самоката')
    def test_scooter_logo_opens_homepage(self, driver):
        main_page = MainPage(driver)

        main_page.click_logo_scooter()

        assert main_page.get_current_url() == MAIN_URL

    @allure.title('Проверка открытия Дзена по логотипу Яндекса')
    def test_yandex_logo_opens_dzen_in_new_tab(self, driver):
        main_page = MainPage(driver)

        main_page.click_logo_yandex()

        assert 'dzen.ru' in main_page.get_current_url()
