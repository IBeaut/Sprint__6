import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    ORDER_TOP = (By.CLASS_NAME, "Button_Button__ra12g")
    ORDER_BOTTOM = (By.XPATH, "//button[text()='Заказать']")

    FAQ_QUESTIONS = (By.CLASS_NAME, "accordion__button")
    FAQ_ANSWERS = (By.CLASS_NAME, "accordion__panel")

    @allure.step("Нажатие на вопрос FAQ под номером {index}")
    def click_faq_question(self, index):
        question = self.find_elements(self.FAQ_QUESTIONS)[index]
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", question)
        self.wait_clickable(self.FAQ_QUESTIONS).click()

    @allure.step("Получение текста ответа FAQ под номером {index}")
    def get_faq_answer_text(self, index):
        answers = self.find_elements(self.FAQ_ANSWERS)
        return answers[index].text.strip()
