import pytest


@pytest.mark.regression
def test_handle(handle_page):
    handle_page.open_page()
    handle_page.handle()
    handle_page.check_title('Пустые рукоятки')
    handle_page.check_full_path('Главная / Магазин / Пустые рукоятки')


@pytest.mark.regression
def test_clear_filters_handle(handle_page):
    handle_page.open_page()
    handle_page.handle()
    handle_page.clear_filters()
    handle_page.check_title('Пустые рукоятки')
    handle_page.check_full_path('Главная / Магазин / Пустые рукоятки')


@pytest.mark.regression
def test_filters(handle_page):
    handle_page.open_page()
    handle_page.handle()
    handle_page.filters('Клинки', 'Эконом')
    handle_page.no_items('Товаров, соответствующих вашему запросу, не обнаружено.')


@pytest.mark.regression
@pytest.mark.parametrize("category, price_range", [
    ('Световые мечи', 'Оптимум'),
    ('Категория «Новичок»', 'Эконом'),
    ('Категория «Мастер»', 'Премиум'),
    ('Категория «Магистр»', 'Эконом'),
    ('Категория «Премиум»', 'Премиум'),
    ('Архив моделей', 'Эконом'),
    ('Электроника', 'Премиум'),
    ('Клинки', 'Эконом'),
    ('Принадлежности', 'Премиум'),
    ('Костюмы', 'Эконом')
])
def test_reset_filters(handle_page, category, price_range):
    handle_page.open_page()
    handle_page.handle()
    handle_page.filters(category, price_range)
    handle_page.reset_filters()
    handle_page.check_title('Пустые рукоятки')
    handle_page.check_full_path('Главная / Магазин / Пустые рукоятки')


@pytest.mark.regression
def test_search(handle_page):
    handle_page.open_page()
    handle_page.handle()
    handle_page.search_item('Рукоять Ben Solo')
    handle_page.check_title('Рукоять Ben Solo')
    handle_page.check_full_path('Главная / Магазин / Пустые рукоятки / Рукоять Ben Solo')


@pytest.mark.regression
def test_zero_search(handle_page):
    handle_page.open_page()
    handle_page.handle()
    handle_page.search_item('testtetstes')
    handle_page.no_items('Товаров, соответствующих вашему запросу, не обнаружено.')


@pytest.mark.regression
def test_english(handle_page):
    handle_page.open_page()
    handle_page.english()
    handle_page.handle()
    handle_page.check_title('Empty hilts')
