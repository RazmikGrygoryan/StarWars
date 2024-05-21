import pytest


@pytest.mark.regression
def test_light_sabers(light_sabers_page):
    light_sabers_page.open_page()
    light_sabers_page.light_sabers()
    light_sabers_page.check_title('Световые мечи')
    light_sabers_page.check_full_path('Главная / Магазин / Световые мечи')


@pytest.mark.regression
def test_clear_filters(light_sabers_page):
    light_sabers_page.open_page()
    light_sabers_page.light_sabers()
    light_sabers_page.clear_filters()
    light_sabers_page.check_title('Световые мечи')
    light_sabers_page.check_full_path('Главная / Магазин / Световые мечи')


@pytest.mark.regression
def test_filters(light_sabers_page):
    light_sabers_page.open_page()
    light_sabers_page.light_sabers()
    light_sabers_page.filters('Категория «Новичок»', 'Эконом')
    light_sabers_page.no_items('Товаров, соответствующих вашему запросу, не обнаружено.')


@pytest.mark.regression
@pytest.mark.parametrize("category, price_range", [
    ('Категория «Ученик»', 'Оптимум'),
    ('Категория «Новичок»', 'Эконом'),
    ('Категория «Мастер»', 'Премиум'),
    ('Категория «Магистр»', 'Эконом'),
    ('Категория «Премиум»', 'Премиум'),
])
def test_reset_filters(light_sabers_page, category, price_range):
    light_sabers_page.open_page()
    light_sabers_page.light_sabers()
    light_sabers_page.filters(category, price_range)
    light_sabers_page.reset_filters()
    light_sabers_page.check_title('Световые мечи')
    light_sabers_page.check_full_path('Главная / Магазин / Световые мечи')


@pytest.mark.regression
def test_search(light_sabers_page):
    light_sabers_page.open_page()
    light_sabers_page.light_sabers()
    light_sabers_page.search_item('Jaw')
    light_sabers_page.check_title('Jaw')
    light_sabers_page.check_full_path('Главная / Магазин / Световые мечи / Категория «Ученик» / Jaw')


@pytest.mark.regression
def test_zero_search(light_sabers_page):
    light_sabers_page.open_page()
    light_sabers_page.light_sabers()
    light_sabers_page.search_item('testtetstes')
    light_sabers_page.no_items('Товаров, соответствующих вашему запросу, не обнаружено.')


@pytest.mark.regression
def test_english(light_sabers_page):
    light_sabers_page.open_page()
    light_sabers_page.english()
    light_sabers_page.light_sabers()
    light_sabers_page.check_title('Premium lightsabers')
