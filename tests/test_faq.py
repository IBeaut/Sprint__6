import pytest
from pages.main_page import MainPage

faq_answers = [
    "Сколько это стоит? И как оплатить?",
    "Хочу сразу несколько самокатов!",
    # Добавь все тексты вопросов/ответов
]

@pytest.mark.faq
@pytest.mark.parametrize("index,text", list(enumerate(faq_answers)))
def test_faq_answer_displayed(browser, index, text):
    page = MainPage(browser)
    page.open("https://qa-scooter.praktikum-services.ru/")
    page.click_faq_question(index)
    assert text in page.get_faq_answer_text(index)
