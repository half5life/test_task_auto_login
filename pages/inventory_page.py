from pages.base_page import BasePage
import allure

class InventoryPage(BasePage):
    PAGE_TITLE = ".title"
    INVENTORY_LIST = ".inventory_list"

    @allure.step("Получить заголовок страницы")
    def get_title(self):
        return self.get_text(self.PAGE_TITLE)

    @allure.step("Проверить видимость списка товаров")
    def is_inventory_list_visible(self):
        return self.page.locator(self.INVENTORY_LIST).is_visible()
