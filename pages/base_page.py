from playwright.sync_api import Page
import allure

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    @allure.step("Открыть страницу {url}")
    def open(self, url):
        self.page.goto(url)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.page.url

    def get_text(self, selector):
        return self.page.locator(selector).text_content()
