from selenium.webdriver.common.by import By


class MainEvent:
    first_katalog = (By.XPATH, '(//*[@class="woocommerce-loop-category__title"])[1]')
    hero_title = (By.CSS_SELECTOR, '[class="hero-title"]')
    full_path_category = (By.CSS_SELECTOR, '[class="woocommerce-breadcrumb"]')
    filters = (By.CSS_SELECTOR, '#woof_widget-4 > div > div > div > div.woof_checkbox_instock_container.woof_container.woof_container_stock.woof_fs_by_instock > div.woof_container_inner > div')
    button_filter = (By.CSS_SELECTOR, '[class="button woof_submit_search_form"]')
    clear_filters = (By.CSS_SELECTOR, '[class="woof_remove_ppi"]')
    category_filter = (By.ID, 'select2-woof_tax_select_product_cat-container')
    first_input = (By.CSS_SELECTOR, 'body > span > span > span.select2-search.select2-search--dropdown > input')
    electronic_category = (By.XPATH, '(//*[@id="select2-woof_tax_select_pa_led-type-container"])[1]')
    second_input = (By.CSS_SELECTOR, 'body > span > span > span.select2-search.select2-search--dropdown > input')
    heroes = (By.CSS_SELECTOR, '[class="select2-search__field"]')
    commerce_info = (By.CSS_SELECTOR, '[class="woocommerce-info"]')
    reset = (By.CSS_SELECTOR, '[class="button woof_reset_search_form"]')
    search_filter = (By.ID, 'wp-block-search__input-2')
    button_search = (By.CSS_SELECTOR, '[aria-label="Поиск"]')
    second_katalog = (By.XPATH, '(//*[@class="woocommerce-loop-category__title"])[2]')
    third_katalog = (By.XPATH, '(//*[@class="woocommerce-loop-category__title"])[3]')
    english = (By.CSS_SELECTOR, '#menu-item-wpml-ls-29-en > a')
