import allure
import pytest
from data import FAQ_ANSWERS
from page_objects.main_page import MainPage


class TestFAQ:

    @allure.title('Проверка полного ответа на вопрос FAQ №{index}')
    @pytest.mark.parametrize(
        'index, expected_answer',
        list(enumerate(FAQ_ANSWERS))
    )
    def test_faq_answer(self, driver, index, expected_answer):
        main_page = MainPage(driver)

        main_page.click_faq_question(index)
        answer = main_page.get_faq_answer(index)

        assert answer == expected_answer
        
