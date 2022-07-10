from .locators import CartPageLocators as CP_locators
from .base_page import BasePage


class CartPage(BasePage):
    def cart_should_be_empty(self):
        assert self.is_not_element_present(*CP_locators.CART_ITEMS)

    def get_cart_content(self):
        cart_content = self.browser.find_element(*CP_locators.CART_CONTENT)
        return cart_content.text
