from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    CART_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_SUBMIT = (By.NAME, 'registration_submit')


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    MESSAGES = (By.CSS_SELECTOR, '#messages')
    ALERT_SUCCESS = (By.CSS_SELECTOR, '.alert-success .alertinner')
    PRODUCT_TITLE = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    CART_PRICE = (By.CSS_SELECTOR, '.basket-mini')


class CartPageLocators():
    CART_CONTENT = (By.CSS_SELECTOR, '#content_inner')
    CART_ITEMS = (By.CSS_SELECTOR, '.basket-items')
