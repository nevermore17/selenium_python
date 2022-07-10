from .pages.main_page import MainPage
from .pages.cart_page import CartPage
from .pages.login_page import LoginPage

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


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"

    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, language):
    link = "http://selenium1py.pythonanywhere.com/"

    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_to_cart_page()

    cart_page = CartPage(browser, browser.current_url)
    cart_page.cart_should_be_empty()
    cart_content = cart_page.get_cart_content()

    assert message_list[language] in cart_content
