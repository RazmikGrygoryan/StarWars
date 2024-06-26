from selenium.webdriver.common.by import By


class LsLocators:
    first_item = (By.CSS_SELECTOR, '[class="button product_type_variable add_to_cart_button wvs-add-to-cart-button wvs_ajax_add_to_cart"]')
    cart = (By.CSS_SELECTOR, '[class="cart-contents button"]')
    name_item = (By.CSS_SELECTOR, '[class="ope-card-product-tile"]')
    cart_name_item = (By.CSS_SELECTOR, '#post-6 > div > div > div.table-box > form > table > tbody > tr.woocommerce-cart-form__cart-item.cart_item > td.product-name > a')
    quantity = (By.CSS_SELECTOR, '[class="input-text qty text"]')
    desc = (By.CSS_SELECTOR, '#page-content > div > div > div.woocommerce-page-content.enabled-sidebars-1.col-sm > div.cart-contents-content > a')
    button_to_cart = (By.CSS_SELECTOR, '#page-content > div > div > div.woocommerce-page-content.enabled-sidebars-1.col-sm > ul > li.wvs-archive-product-wrapper.product.type-product.post-27219.status-publish.first.instock.product_cat-master.product_tag-darth-vader.has-post-thumbnail.shipping-taxable.purchasable.product-type-variable.has-default-attributes.berocket_lmp_first_on_page > div > div.ope-woo-card-footer > a.button.product_type_variable.add_to_cart_button.wvs-add-to-cart-button.wvs_ajax_add_to_cart.added')
    remove = (By.CSS_SELECTOR, '[class="remove"]')
    cart_info = (By.CSS_SELECTOR, '[class="cart-empty woocommerce-info"]')
    deleted_item = (By.CSS_SELECTOR, '[class="woocommerce-message"]')
    button_plus = (By.CSS_SELECTOR, '[class="quantity__btn plus"]')
    button_minus = (By.CSS_SELECTOR, '[class="quantity__btn minus"]')
    update_cart = (By.CSS_SELECTOR, '[name="update_cart"]')
    info_message = (By.CSS_SELECTOR, '[class="woocommerce-message"]')
    coupone_code = (By.CSS_SELECTOR, '[name="coupon_code"]')
    apply_coupone = (By.CSS_SELECTOR, '[name="apply_coupon"]')
    error_message = (By.CSS_SELECTOR, '[class="woocommerce-error"]')
    forward = (By.CSS_SELECTOR, '[class="checkout-button button alt wc-forward"]')
    first_name = (By.CSS_SELECTOR, '[name="billing_first_name"]')
    second_name = (By.CSS_SELECTOR, '[name="billing_last_name"]')
    city = (By.CSS_SELECTOR, '#billing_city_field > span > span > span.selection > span > span.select2-selection__arrow')
    input_city = (By.CSS_SELECTOR, 'body > span > span > span.select2-search.select2-search--dropdown > input')
    choose_city = (By.CSS_SELECTOR, '#\\34 4 > div')
    address = (By.CSS_SELECTOR, '[name="billing_address_1"]')
    optional_address = (By.CSS_SELECTOR, '[name="billing_address_2"]')
    postcode = (By.CSS_SELECTOR, '[name="billing_postcode"]')
    phone = (By.CSS_SELECTOR, '[name="billing_phone"]')
    email = (By.CSS_SELECTOR, '[name="billing_email"]')
    buy_checkbox = (By.XPATH, '(//*[@class="woocommerce-form__input woocommerce-form__input-checkbox input-checkbox"])[2]')
    buy = (By.ID, 'place_order')
    check_tinkoff = (By.CSS_SELECTOR, '[automation-id="payment-item__title"]')
    block = (By.XPATH, '(//*[@class="blockUI blockOverlay"])[2]')
    error_first_name = (By.CSS_SELECTOR, '[data-id="billing_first_name"]')
    error_second_name = (By.CSS_SELECTOR, '[data-id="billing_last_name"]')
    error_city = (By.CSS_SELECTOR, '[data-id="billing_city"]')
    error_adress = (By.CSS_SELECTOR, '[data-id="billing_address_1"]')
    error_post_code = (By.CSS_SELECTOR, '[data-id="billing_postcode"]')
    error_phone = (By.CSS_SELECTOR, '[data-id="billing_phone"]')
    error_email = (By.CSS_SELECTOR, '[data-id="billing_email"]')
    error_info = (By.CSS_SELECTOR, '#post-7 > div > div > form.checkout.woocommerce-checkout > div.woocommerce-NoticeGroup.woocommerce-NoticeGroup-checkout > ul > li:nth-child(8)')
    email_alert = (By.CSS_SELECTOR, '#post-7 > div > div > form.checkout.woocommerce-checkout > div.woocommerce-NoticeGroup.woocommerce-NoticeGroup-checkout > ul > li')
    phone_alert = (By.CSS_SELECTOR, '[data-id="billing_phone"]')