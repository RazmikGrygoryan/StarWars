import pytest


@pytest.mark.smoke
def test_two_items(items_page):
    items_page.open_page()
    items_page.items()
    items_page.check_title('Корзина')


@pytest.mark.smoke
def test_remove(items_page):
    items_page.open_page()
    items_page.items()
    items_page.remove('Ваша корзина пока пуста.')
    items_page.check_title('Корзина')


@pytest.mark.smoke
def test_update_cart(items_page):
    items_page.open_page()
    items_page.items()
    items_page.update_cart('Корзина обновлена.')
    items_page.check_title('Корзина')


@pytest.mark.smoke
@pytest.mark.parametrize("promo", [
        'test',
        '1',
        'star wars',
    ])
def test_coupone_error(items_page, promo):
    items_page.open_page()
    items_page.items()
    items_page.promocode(promo, f"Купона «{promo}» не существует!")


@pytest.mark.smoke
def test_buy_items(items_page):
    items_page.open_page()
    items_page.items()
    items_page.buy_items('Test', 'Test', 'Москва', 'test', 'test', '0022', '+79788889876', 'test@gmail.com')
    items_page.check_tinkoff('Быстрая оплата')


@pytest.mark.smoke
def test_check_incorrect_email(items_page):
    items_page.open_page()
    items_page.items()
    items_page.buy_items('Test', 'Test', 'Москва', 'test', 'test', '0022', '+79788889876', 'dfsdfsdf')
    items_page.check_email('Неверный адрес эл. почты для выставления счета')


@pytest.mark.smoke
def test_check_incorrect_phone(items_page):
    items_page.open_page()
    items_page.items()
    items_page.buy_items('Test', 'Test', 'Москва', 'test', 'test', '0022', 'sdfsadfsad', 'test@gmail.com')
    items_page.check_phone('Платежи Телефон не является корректным номером телефона.')


@pytest.mark.smoke
def test_error_messages(items_page):
    items_page.open_page()
    items_page.items()
    items_page.error_messages(
        'Платежи Имя является обязательным полем.',
        'Платежи Фамилия является обязательным полем.',
        'Платежи Населённый пункт является обязательным полем.',
        'Платежи Адрес является обязательным полем.',
        'Платежи Почтовый индекс является обязательным полем.',
        'Платежи Телефон является обязательным полем.',
        'Платежи Email является обязательным полем.',
        'Чтобы продолжить оформление заказа, прочитайте правила и условия и подтвердите своё согласие с ними.'
    )
