import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage


class ConfirmationPage(BasePage):
    SUCCESS_MESSAGE = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")

    @allure.step("Получение текста подтверждения заказа")
    def get_success_message(self):
        return self.find_element(self.SUCCESS_MESSAGE).text
