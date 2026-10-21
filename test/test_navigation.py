from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from page_objects.main_page import MainPage


class TestNavigation:

    def test_order_button_bottom_opens_form(self, driver):
        main_page = MainPage(driver)

        # Нажимаем нижнюю кнопку «Заказать»
        main_page.click_order_button_bottom()

        # Проверяем, что появилась форма заказа
        order_form = WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Для кого самокат')]")
            )
        )

        assert order_form.is_displayed()

    def test_scooter_logo_opens_homepage(self, driver):
        main_page = MainPage(driver)

        # Нажимаем на логотип «Самоката»
        main_page.click_logo_scooter()

        # Проверяем адрес главной страницы
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    def test_yandex_logo_opens_dzen_in_new_tab(self, driver):
        main_page = MainPage(driver)
        original_window = driver.current_window_handle

        # Нажимаем на логотип Яндекса
        main_page.click_logo_yandex()

        # Ждём открытия новой вкладки
        WebDriverWait(driver, 15).until(
            expected_conditions.number_of_windows_to_be(2)
        )

        # Переключаемся на новую вкладку
        for window in driver.window_handles:
            if window != original_window:
                driver.switch_to.window(window)
                break

        # Ждём перехода на Дзен
        WebDriverWait(driver, 20).until(
            lambda browser: 'dzen.ru' in browser.current_url
        )

        assert 'dzen.ru' in driver.current_url