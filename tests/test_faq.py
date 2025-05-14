import pytest
import allure
from pages.main_page import MainPage

faq_answers = [
    "Сколько это стоит? И как оплатить?",
    "Хочу сразу несколько самокатов!"
    # Добавь все нужные вопросы по порядку
]

@pytest.mark.faq
@pytest.mark.parametrize("index,text", list(enumerate(faq_answers)))
@allure.title("Проверка FAQ: {text}")
def test_faq_answer_displayed(browser, index, text):
    page = MainPage(browser)
    page.open("https://qa-scooter.praktikum-services.ru/")
    page.click_faq_question(index)
    assert text in page.get_faq_answer_text(index)
