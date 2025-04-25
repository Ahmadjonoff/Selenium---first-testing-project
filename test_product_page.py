from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.locators import BasketPageLocators, BasePageLocators
import pytest, time

# links = [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}" for i in range(10)]

# @pytest.mark.parametrize('link', links)
# def test_guest_can_add_product_to_basket(browser, link):
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.add_product_to_basket()
#     product_page.should_be_added_successfully()

# @pytest.mark.xfail(reason="Success message is presented")
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_product_to_basket()
#     page.should_not_be_success_message()

# def test_guest_cant_see_success_message(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_not_be_success_message()

# @pytest.mark.xfail(reason="Success msg is presented")
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_product_to_basket()
#     page.should_not_be_succ_mess_via_is_disappeared()

# def test_guest_should_see_login_link(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()

# def test_guest_can_go_to_login_page_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_login_page()
#     login_page = LoginPage(browser, browser.current_url)
#     login_page.should_be_login_link()

# def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.go_to_basket_page()
#     basket_page = BasketPage(browser, browser.current_url)
#     basket_page.should_be_not_products()
#     basket_page.should_be_empty_text()

@pytest.mark.add_to_basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.browser = browser
        login_link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(self.browser, login_link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "Strongp@assword1234"
        page.register_new_user(email, password)
        page.should_be_authorized_user()
        
    def test_user_cant_see_success_message(self):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(self.browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
        product_page = ProductPage(self.browser, link)
        product_page.open()
        product_page.add_product_to_basket()
        product_page.should_be_added_successfully()