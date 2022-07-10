from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage
import pytest
import time

test_links = [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param(
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
        marks=pytest.mark.xfail
    ),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
]

message_list = {
    "ar": "سلة التسوق فارغة",
    "ca": "La seva cistella està buida.",
    "cs": "Váš košík je prázdný.",
    "da": "Din indkøbskurv er tom.",
    "de": "Ihr Warenkorb ist leer.",
    "en": "Your basket is empty.",
    "el": "Το καλάθι σας είναι άδειο.",
    "es": "Tu carrito esta vacío.",
    "fi": "Korisi on tyhjä",
    "fr": "Votre panier est vide.",
    "it": "Il tuo carrello è vuoto.",
    "ko": "장바구니가 비었습니다.",
    "nl": "Je winkelmand is leeg",
    "pl": "Twój koszyk jest pusty.",
    "pt": "O carrinho está vazio.",
    "pt-br": "Sua cesta está vazia.",
    "ro": "Cosul tau este gol.",
    "ru": "Ваша корзина пуста",
    "sk": "Váš košík je prázdny",
    "uk": "Ваш кошик пустий.",
    "zh-cn": "Your basket is empty.",
}


@pytest.mark.need_review
@pytest.mark.parametrize('link', test_links)
def test_guest_can_add_product_to_cart(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.schuld_have_add_to_cart_button()
    product_page.add_product_to_cart()
    product_page.solve_quiz_and_get_code()

    success_message_text = product_page.get_success_message_text()

    product_title = product_page.get_product_title()

    assert product_title in success_message_text

    product_price = product_page.get_product_price()
    cart_price = product_page.get_cart_price()

    assert product_price == cart_price


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/studyguide-for-counter-hack-reloaded_205/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.schuld_have_add_to_cart_button()
    product_page.add_product_to_cart()
    product_page.schuld_success_message_is_not_present()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/studyguide-for-counter-hack-reloaded_205/'

    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.schuld_success_message_is_not_present()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/studyguide-for-counter-hack-reloaded_205/'

    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.schuld_have_add_to_cart_button()
    product_page.add_product_to_cart()
    product_page.schuld_success_message_disappear()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, language):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"

    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_cart_page()

    cart_page = CartPage(browser, browser.current_url)
    cart_page.cart_should_be_empty()

    cart_content = cart_page.get_cart_content()

    assert message_list[language] in cart_content


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"

    main_page = ProductPage(browser, link)
    main_page.open()
    main_page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.register_new_user(
            f'Login{str(time.time())}',
            f'{str(time.time())}@fakemail.com')

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"

        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.schuld_have_add_to_cart_button()
        product_page.add_product_to_cart()
        product_page.solve_quiz_and_get_code()

        success_message_text = product_page.get_success_message_text()

        product_title = product_page.get_product_title()

        assert product_title in success_message_text

        product_price = product_page.get_product_price()
        cart_price = product_page.get_cart_price()

        assert product_price == cart_price

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/studyguide-for-counter-hack-reloaded_205/'

        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.schuld_success_message_is_not_present()
