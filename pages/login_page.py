from pages.base_page import BasePage
import allure

class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    USERNAME_INPUT = "[data-test='username']"
    PASSWORD_INPUT = "[data-test='password']"
    LOGIN_BUTTON = "[data-test='login-button']"
    ERROR_MESSAGE = "[data-test='error']"

    @allure.step("Открыть страницу логина")
    def open(self):
        super().open(self.URL)

    @allure.step("Выполнить вход с логином '{username}' и паролем '{password}'")
    def login(self, username, password):
        self.page.locator(self.USERNAME_INPUT).fill(username)
        self.page.locator(self.PASSWORD_INPUT).fill(password)
        self.page.locator(self.LOGIN_BUTTON).click()

    @allure.step("Получить сообщение об ошибке")
    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
