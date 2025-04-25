from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, '//a[@class="btn btn-default"][contains(@href, "basket")]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL = (By.CSS_SELECTOR, "input[name='registration-email']")
    REG_PASS = (By.CSS_SELECTOR, "input[name='registration-password1']")
    REG_PASS2 = (By.CSS_SELECTOR, "input[name='registration-password2']")
    REG_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]') 

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ALERT_ADDED_TO_CART = (By.CSS_SELECTOR, ".alert-success")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, "div.alertinner strong")
    ADDED_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alert-noicon.alert-info p strong")

class BasketPageLocators():
    PRODUCTS_LINK = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_TEXT_LINK = (By.CSS_SELECTOR, '#content_inner > p')