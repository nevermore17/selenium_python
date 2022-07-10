from .base_page import BasePage
from .locators import LoginPageLocators as LP_locators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_input = self.browser.find_element(
            *LP_locators.REGISTRATION_EMAIL
        )
        email_input.send_keys(email)

        password1_input = self.browser.find_element(
            *LP_locators.REGISTRATION_PASSWORD1
        )
        password1_input.send_keys(password)

        password2_input = self.browser.find_element(
            *LP_locators.REGISTRATION_PASSWORD1
        )
        password2_input.send_keys(password)

        registration_submit = self.browser.find_element(
            *LP_locators.REGISTRATION_SUBMIT
        )
        registration_submit.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LP_locators.LOGIN_FORM), 'Login form is not found'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LP_locators.REGISTER_FORM), 'Register form is not found'
