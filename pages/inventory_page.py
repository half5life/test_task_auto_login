from pages.base_page import BasePage

class InventoryPage(BasePage):
    PAGE_TITLE = ".title"
    INVENTORY_LIST = ".inventory_list"

    def get_title(self):
        return self.get_text(self.PAGE_TITLE)

    def is_inventory_list_visible(self):
        return self.page.locator(self.INVENTORY_LIST).is_visible()
