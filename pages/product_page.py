from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button.click()
        self.solve_quiz_and_get_code()

    def should_be_added_successfully(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_ADDED_TO_CART), "Product is not added"

        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        added_product_price = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE).text

        assert product_name == added_product_name, f"The alert contains wrong product name: {added_product_name} - {product_name}"
        assert product_price == added_product_price,  f"Product cost in cart is not equal to the product cost {added_product_price} != {product_price}"
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_ADDED_TO_CART), "Success message is presented, but should not be"

    def should_not_be_succ_mess_via_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_ADDED_TO_CART), "Success message is presented, but should not be"