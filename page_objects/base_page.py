import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Найти элемент')
    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(locator)
        )

    @allure.step('Найти элементы')
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step('Нажать на элемент')
    def click_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(locator)
        ).click()

    @allure.step('Ввести текст в поле')
    def send_keys_to_element(self, locator, text):
        self.find_element(locator).send_keys(text)

    @allure.step('Дождаться появления элемента')
    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 15).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    @allure.step('Прокрутить страницу к элементу')
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

    @allure.step('Нажать на элемент через JavaScript')
    def click_element_with_js(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script(
            "arguments[0].click();",
            element
        )

    @allure.step('Получить текущий адрес страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Получить текущий идентификатор окна')
    def get_current_window_handle(self):
        return self.driver.current_window_handle

    @allure.step('Получить открытые окна браузера')
    def get_window_handles(self):
        return self.driver.window_handles

    @allure.step('Дождаться открытия нужного количества окон')
    def wait_for_window_count(self, count):
        WebDriverWait(self.driver, 15).until(
            expected_conditions.number_of_windows_to_be(count)
        )

    @allure.step('Переключиться на окно браузера')
    def switch_to_window(self, window_handle):
        self.driver.switch_to.window(window_handle)

    @allure.step('Переключиться на новую вкладку')
    def switch_to_new_window(self, original_window):
        self.wait_for_window_count(2)

        for window in self.get_window_handles():
            if window != original_window:
                self.switch_to_window(window)
                break

    @allure.step('Дождаться адреса, содержащего текст')
    def wait_for_url_contains(self, text):
        WebDriverWait(self.driver, 20).until(
            expected_conditions.url_contains(text)
        )

    @allure.step('Развернуть окно браузера')
    def maximize_window(self):
        self.driver.maximize_window()

    @allure.step('Открыть страницу')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Закрыть браузер')
    def quit_browser(self):
        self.driver.quit()