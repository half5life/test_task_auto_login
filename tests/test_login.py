import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_successful_login(page):
    """
    Проверка успешного входа в систему под стандартным пользователем.
    """
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open()

    login_page.login("standard_user", "secret_sauce")

    assert "inventory.html" in login_page.get_current_url(), "URL должен содержать 'inventory.html'"

    assert inventory_page.is_inventory_list_visible(), "Список товаров должен быть виден"
    assert inventory_page.get_title() == "Products", "Заголовок страницы должен быть 'Products'"


def test_login_with_wrong_password(page):
    """
    Проверка сообщения об ошибке при вводе неверного пароля.
    """
    login_page = LoginPage(page)
    login_page.open()
    
    login_page.login("standard_user", "wrong_password")

    expected_error = "Epic sadface: Username and password do not match any user in this service"
    assert login_page.get_error_message() == expected_error


def test_locked_out_user(page):
    """
    Проверка сообщения об ошибке для заблокированного пользователя.
    """
    login_page = LoginPage(page)
    login_page.open()
    
    login_page.login("locked_out_user", "secret_sauce")

    expected_error = "Epic sadface: Sorry, this user has been locked out."
    assert login_page.get_error_message() == expected_error


def test_empty_fields(page):
    """
    Проверка валидации при пустых полях (просто клик по кнопке Login).
    """
    login_page = LoginPage(page)
    login_page.open()
    
    login_page.login("", "")

    expected_error = "Epic sadface: Username is required"
    assert login_page.get_error_message() == expected_error


def test_performance_glitch_user(page):
    """
    Проверка входа пользователя с задержкой загрузки (performance_glitch_user).
    Playwright по умолчанию ждет элементы до 30 секунд, поэтому тест должен пройти
    так же, как и обычный успешный логин, просто чуть дольше.
    """
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open()
    login_page.login("performance_glitch_user", "secret_sauce")

    # Проверки аналогичны успешному логину
    assert "inventory.html" in login_page.get_current_url()
    assert inventory_page.is_inventory_list_visible()
