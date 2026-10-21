import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from page_objects.main_page import MainPage


class TestFAQ:

    @pytest.mark.parametrize('index, expected_answer', [
        (0, 'Сутки — 400 рублей.'),
        (1, 'один заказ — один самокат'),
        (2, 'Отсчёт времени аренды начинается с момента'),
        (3, 'Только начиная с завтрашнего дня.'),
        (4, 'Пока что нет!'),
        (5, 'Самокат приезжает к вам с полной зарядкой.'),
        (6, 'Да, пока самокат не привезли.'),
        (7, 'Да, обязательно.')
    ])
    def test_faq_answer(self, driver, index, expected_answer):
        question_locator = (
            MainPage.FAQ_QUESTION[0],
            MainPage.FAQ_QUESTION[1].format(index)
        )

        answer_locator = (
            MainPage.FAQ_ANSWER[0],
            MainPage.FAQ_ANSWER[1].format(index)
        )

        question = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located(
                question_locator
            )
        )

        driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            question
        )

        # Нажимаем на вопрос, даже если его перекрывает картинка
        driver.execute_script(
            "arguments[0].click();",
            question
        )

        answer = WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(
                answer_locator
            )
        )

        assert expected_answer in answer.text