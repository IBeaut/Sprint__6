from selenium.webdriver.common.by import By
from .base_page import BasePage

class ConfirmationPage(BasePage):
    SUCCESS_MESSAGE = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)
