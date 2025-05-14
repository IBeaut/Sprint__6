from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class OrderPage(BasePage):
    # Шаг 1
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.CLASS_NAME, "select-search__input")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Шаг 2
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    RENT_OPTIONS = (By.CLASS_NAME, "Dropdown-option")

    COLOR_BLACK = (By.ID, "black")
    COLOR_GRAY = (By.ID, "grey")

    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")

    def fill_user_info(self, name, surname, address, metro, phone):
        self.driver.find_element(*self.NAME).send_keys(name)
        self.driver.find_element(*self.SURNAME).send_keys(surname)
        self.driver.find_element(*self.ADDRESS).send_keys(address)

        metro_input = self.driver.find_element(*self.METRO_INPUT)
        metro_input.click()
        metro_input.send_keys(metro)
        option = (By.XPATH, f"//button/div[text()='{metro}']")
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(option)).click()

        self.driver.find_element(*self.PHONE).send_keys(phone)
        self.driver.find_element(*self.NEXT_BUTTON).click()

    def fill_rent_info(self, date, rent_days_index=1, color="black", comment=""):
        self.driver.find_element(*self.DATE_INPUT).click()

        target_day = date.split('.')[0].lstrip('0')
        target_month = date.split('.')[1].lstrip('0')
        target_year = date.split('.')[2]

        while True:
            visible_month = self.driver.find_element(By.CLASS_NAME, "react-datepicker__current-month").text
            if target_year in visible_month:
                break
            self.driver.find_element(By.CLASS_NAME, "react-datepicker__navigation--next").click()
            WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((By.CLASS_NAME, "react-datepicker"))
            )

        day_selector = (By.XPATH, f"//div[contains(@class,'react-datepicker__day') and text()='{target_day}']")
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(day_selector)).click()

        self.driver.find_element(*self.RENT_DROPDOWN).click()
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_all_elements_located(self.RENT_OPTIONS)
        )[rent_days_index].click()

        if color.lower() == "black":
            self.driver.find_element(*self.COLOR_BLACK).click()
        elif color.lower() in ("gray", "grey"):
            self.driver.find_element(*self.COLOR_GRAY).click()

        self.driver.find_element(*self.COMMENT_INPUT).send_keys(comment)

        self.driver.find_element(*self.ORDER_BUTTON).click()
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.CONFIRM_BUTTON)
        ).click()
