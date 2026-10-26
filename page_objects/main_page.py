import allure
from page_objects.base_page import BasePage
from locators.locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Нажать верхнюю кнопку «Заказать»')
    def click_order_button_header(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_HEADER)

    @allure.step('Нажать нижнюю кнопку «Заказать»')
    def click_order_button_bottom(self):
        cookie_buttons = self.find_elements(
            MainPageLocators.COOKIE_BUTTON
        )
        if cookie_buttons:
            self.click_element(MainPageLocators.COOKIE_BUTTON)

        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click_element(MainPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step('Нажать на логотип Самоката')
    def click_logo_scooter(self):
        self.click_element(MainPageLocators.LOGO_SCOOTER)

    @allure.step('Нажать на логотип Яндекса')
    def click_logo_yandex(self):
        original_window = self.get_current_window_handle()
        self.click_element(MainPageLocators.LOGO_YANDEX)
        self.switch_to_new_window(original_window)
        self.wait_for_url_contains('dzen.ru')

    @allure.step('Открыть ответ на вопрос FAQ')
    def click_faq_question(self, index):
        question_locator = (
            MainPageLocators.FAQ_QUESTION[0],
            MainPageLocators.FAQ_QUESTION[1].format(index)
        )

        answer_locator = (
            MainPageLocators.FAQ_ANSWER[0],
            MainPageLocators.FAQ_ANSWER[1].format(index)
        )
        self.scroll_to_element(question_locator)
        self.click_element_with_js(question_locator)
        self.wait_for_element(answer_locator)

    @allure.step('Получить ответ FAQ')
    def get_faq_answer(self, index):
        answer_locator = (
            MainPageLocators.FAQ_ANSWER[0],
            MainPageLocators.FAQ_ANSWER[1].format(index)
        )

        return self.wait_for_element(answer_locator).text

    @allure.step('Проверить отображение формы заказа')
    def is_order_form_visible(self):
        return self.wait_for_element(
            MainPageLocators.ORDER_FORM_TITLE
        ).is_displayed()