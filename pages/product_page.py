from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from .locators import ProductPageLocators as PP_locators
import re


class ProductPage(BasePage):
    def schuld_have_add_to_cart_button(self):
        assert self.is_element_present(
            *PP_locators.ADD_TO_CART_BUTTON
        ), 'Add_to_cart_btn not found'

    def add_product_to_cart(self):
        add_to_cart_button = self.browser.find_element(
            *PP_locators.ADD_TO_CART_BUTTON
        )
        add_to_cart_button.click()

    def get_product_title(self):
        return self.browser.find_element(*PP_locators.PRODUCT_TITLE).text

    def get_product_price(self):
        text = self.browser.find_element(*PP_locators.PRODUCT_PRICE).text
        return re.search(r'\d+[\.,]\d+', text).group()

    def get_cart_price(self):
        text = self.browser.find_element(*PP_locators.CART_PRICE).text
        return re.search(r'\d+[\.,]\d+', text).group()

    def schuld_success_message_is_not_present(self):
        assert self.is_not_element_present(*PP_locators.ALERT_SUCCESS), 'Success message is present on page'

    def schuld_success_message_disappear(self):
        assert self.is_disappeared(*PP_locators.ALERT_SUCCESS), 'Success message is not dissapear'

    def get_success_message_text(self):
        try:
            messages = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located(PP_locators.MESSAGES)
            )
        except TimeoutException:
            print('Messages not found on page in time')

        alert_success_list = messages.find_elements(*PP_locators.ALERT_SUCCESS)

        assert len(alert_success_list) != 0, 'Alert success messages is not found'

        return alert_success_list[0].text


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
