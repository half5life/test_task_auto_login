from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url):
        self.page.goto(url)

    def get_current_url(self):
        return self.page.url

    def get_text(self, selector):
        return self.page.locator(selector).text_content()
