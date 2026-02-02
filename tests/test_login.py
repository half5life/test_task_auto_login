import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@allure.feature("Login Scenarios")
class TestLogin:
    
    @allure.story("Positive Login")
    @allure.title("Успешный вход (Standard User)")
    def test_successful_login(self, page):
        """
        Проверка успешного входа в систему под стандартным пользователем.
        """
        login_page = LoginPage(page)
        inventory_page = InventoryPage(page)

        login_page.open()

        login_page.login("standard_user", "secret_sauce")

        with allure.step("Проверить, что произошел переход на страницу инвентаря"):
            assert "inventory.html" in login_page.get_current_url(), "URL должен содержать 'inventory.html'"

        with allure.step("Проверить видимость списка товаров"):
            assert inventory_page.is_inventory_list_visible(), "Список товаров должен быть виден"
            assert inventory_page.get_title() == "Products", "Заголовок страницы должен быть 'Products'"


    @allure.story("Negative Login")
    @allure.title("Вход с неверным паролем")
    def test_login_with_wrong_password(self, page):
        """
        Проверка сообщения об ошибке при вводе неверного пароля.
        """
        login_page = LoginPage(page)
        login_page.open()
        
        login_page.login("standard_user", "wrong_password")

        expected_error = "Epic sadface: Username and password do not match any user in this service"
        with allure.step("Проверить текст ошибки"):
            assert login_page.get_error_message() == expected_error


    @allure.story("Negative Login")
    @allure.title("Вход заблокированного пользователя")
    def test_locked_out_user(self, page):
        """
        Проверка сообщения об ошибке для заблокированного пользователя.
        """
        login_page = LoginPage(page)
        login_page.open()
        
        login_page.login("locked_out_user", "secret_sauce")

        expected_error = "Epic sadface: Sorry, this user has been locked out."
        with allure.step("Проверить текст ошибки"):
            assert login_page.get_error_message() == expected_error


    @allure.story("Negative Login")
    @allure.title("Вход с пустыми полями")
    def test_empty_fields(self, page):
        """
        Проверка валидации при пустых полях (просто клик по кнопке Login).
        """
        login_page = LoginPage(page)
        login_page.open()
        
        login_page.login("", "")

        expected_error = "Epic sadface: Username is required"
        with allure.step("Проверить текст ошибки"):
            assert login_page.get_error_message() == expected_error


    @allure.story("Performance Login")
    @allure.title("Вход пользователя с задержкой (Performance Glitch User)")
    def test_performance_glitch_user(self, page):
        """
        Проверка входа пользователя с задержкой загрузки.
        """
        login_page = LoginPage(page)
        inventory_page = InventoryPage(page)

        login_page.open()
        login_page.login("performance_glitch_user", "secret_sauce")

        with allure.step("Проверить успешный вход"):
            assert "inventory.html" in login_page.get_current_url()
            assert inventory_page.is_inventory_list_visible()
