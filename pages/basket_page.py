from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_not_products(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_LINK), "Basket is not empty"

    def should_be_empty_text(self):
        text = self.browser.find_elements(*BasketPageLocators.EMPTY_TEXT_LINK)
        assert len(text) == 1, "Basket is not empty, empty text is not presented"