from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class MainPage(BasePage):
    ORDER_TOP = (By.CLASS_NAME, "Button_Button__ra12g")
    ORDER_BOTTOM = (By.XPATH, "//button[text()='Заказать']")

    FAQ_QUESTIONS = (By.CLASS_NAME, "accordion__button")
    FAQ_ANSWERS = (By.CLASS_NAME, "accordion__panel")

    def click_faq_question(self, index):
        question = self.driver.find_elements(*self.FAQ_QUESTIONS)[index]
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", question)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(question)).click()

    def get_faq_answer_text(self, index):
        answers = self.driver.find_elements(*self.FAQ_ANSWERS)
        WebDriverWait(self.driver, 5).until(EC.visibility_of(answers[index]))
        return answers[index].text.strip()
