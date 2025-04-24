from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_not_products(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_LINK), "Product is presented, but basket should be empty"

    def should_be_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_TEXT_LINK), "Empty text is not presented"