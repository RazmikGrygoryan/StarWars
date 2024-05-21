import pytest


@pytest.mark.regression
def test_accessories(accessories_page):
    accessories_page.open_page()
    accessories_page.accessories()
    accessories_page.check_title('Аксессуары')
    accessories_page.check_full_path('Главная / Магазин / Аксессуары')


@pytest.mark.regression
def test_clear_filters_accessories(accessories_page):
    accessories_page.open_page()
    accessories_page.accessories()
    accessories_page.clear_filters()
    accessories_page.check_title('Аксессуары')
    accessories_page.check_full_path('Главная / Магазин / Аксессуары')


@pytest.mark.regression
def test_filters(accessories_page):
    accessories_page.open_page()
    accessories_page.accessories()
    accessories_page.filters('Клинки', 'Эконом')
    accessories_page.no_items('Товаров, соответствующих вашему запросу, не обнаружено.')


@pytest.mark.regression
@pytest.mark.parametrize("category, price_range", [
    ('Электроника', 'Оптимум'),
    ('Клинки', 'Эконом'),
    ('Принадлежности', 'Премиум'),
    ('Костюмы', 'Эконом'),
])
def test_reset_filters(accessories_page, category, price_range):
    accessories_page.open_page()
    accessories_page.accessories()
    accessories_page.filters(category, price_range)
    accessories_page.reset_filters()
    accessories_page.check_title('Аксессуары')
    accessories_page.check_full_path('Главная / Магазин / Аксессуары')


@pytest.mark.regression
def test_search(accessories_page):
    accessories_page.open_page()
    accessories_page.accessories()
    accessories_page.search_item('Костюм Ситха')
    accessories_page.check_title('Костюм Ситха')
    accessories_page.check_full_path('Главная / Магазин / Аксессуары / Костюмы / Костюм Ситха')


@pytest.mark.regression
def test_zero_search(accessories_page):
    accessories_page.open_page()
    accessories_page.accessories()
    accessories_page.search_item('testtetstes')
    accessories_page.no_items('Товаров, соответствующих вашему запросу, не обнаружено.')


@pytest.mark.regression
def test_english(accessories_page):
    accessories_page.open_page()
    accessories_page.english()
    accessories_page.accessories()
    accessories_page.check_title('Accessories')
