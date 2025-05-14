import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.confirmation_page import ConfirmationPage

order_data = [
    ("Иван", "Иванов", "ул. Ленина, д.1", "Черкизовская", "89991112233", "12.06.2025", 1, "black", "Позвоните заранее"),
    ("Пётр", "Сидоров", "ул. Пушкина, д.10", "Арбатская", "80001234567", "15.06.2025", 2, "gray", "Без звонка"),
]

@pytest.mark.order
@pytest.mark.parametrize("button", ["top", "bottom"])
@pytest.mark.parametrize("name, surname, address, metro, phone, date, rent_index, color, comment", order_data)
@allure.title("Оформление заказа через кнопку {button}")
def test_order_flow(browser, name, surname, address, metro, phone, date, rent_index, color, comment, button):
    main = MainPage(browser)
    main.open("https://qa-scooter.praktikum-services.ru/")

    if button == "top":
        main.click(MainPage.ORDER_TOP)
    else:
        main.click(MainPage.ORDER_BOTTOM)

    order = OrderPage(browser)
    order.fill_user_info(name, surname, address, metro, phone)
    order.fill_rent_info(date, rent_index, color, comment)

    confirmation = ConfirmationPage(browser)
    success_text = confirmation.get_success_message()
    assert "Заказ оформлен" in success_text or "успешно" in success_text
