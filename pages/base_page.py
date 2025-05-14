import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    @allure.step("Открытие страницы: {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Поиск одного элемента: {locator}")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Поиск всех элементов: {locator}")
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Ожидание кликабельности элемента: {locator}")
    def wait_clickable(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Ожидание видимости элемента: {locator}")
    def wait_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Клик по элементу: {locator}")
    def click(self, locator):
        self.wait_clickable(locator).click()
