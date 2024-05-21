from pages.base_page import BasePage
from pages.locators.items_locators import LsLocators
from pages.locators.main_locators import MainEvent
from selenium.webdriver.common.keys import Keys
import allure


class Items(BasePage):
    page_url = 'shop/category/lightsabers/master/'

    @allure.step('Add to cart items')
    def items(self):
        self.element_is_visible(LsLocators.first_item).click()
        self.element_is_visible(LsLocators.button_to_cart).click()
        self.text_name = self.element_is_visible(LsLocators.name_item).text
        desc = self.element_is_visible(LsLocators.desc).text
        self.element_is_visible(LsLocators.cart).click()
        cart_text_name = self.element_is_visible(LsLocators.cart_name_item).text
        qty = self.element_is_visible(LsLocators.quantity).text
        assert self.text_name.lower() in cart_text_name.lower()
        assert qty in desc

    @allure.step('Check title')
    def check_title(self, text):
        title = self.element_is_visible(MainEvent.hero_title)
        assert title.text == text

    @allure.step('Remove items in cart')
    def remove(self, text):
        self.element_is_visible(LsLocators.remove).click()
        info = self.element_is_visible(LsLocators.cart_info)
        deleted_item = self.element_is_visible(LsLocators.deleted_item).text
        assert info.text == text
        assert self.text_name.lower() in deleted_item.lower()

    @allure.step('Update cart')
    def update_cart(self, text):
        self.element_is_visible(LsLocators.button_plus).click()
        self.element_is_visible(LsLocators.button_plus).click()
        self.element_is_visible(LsLocators.button_minus).click()
        self.element_is_visible(LsLocators.update_cart).click()
        info = self.element_is_visible(LsLocators.info_message)
        assert info.text == text

    @allure.step('Add promo')
    def promocode(self, promo, text):
        self.element_is_visible(LsLocators.coupone_code).send_keys(promo)
        self.element_is_visible(LsLocators.apply_coupone).click()
        error = self.element_is_visible(LsLocators.error_message).text
        assert error == text

    @allure.step('Buy items')
    def buy_items(self, first_name, second_name, city, address, optional_address, postcode, phone, email):
        self.element_is_visible(LsLocators.forward).click()
        self.element_is_visible(LsLocators.first_name).send_keys(first_name)
        self.element_is_visible(LsLocators.second_name).send_keys(second_name)
        self.element_is_visible(LsLocators.city).click()
        self.element_is_visible(LsLocators.input_city).send_keys(city)
        self.element_is_visible(LsLocators.choose_city).click()
        self.element_is_visible(LsLocators.address).send_keys(address)
        self.element_is_visible(LsLocators.optional_address).send_keys(optional_address)
        self.element_is_visible(LsLocators.postcode).send_keys(postcode)
        self.element_is_visible(LsLocators.phone).send_keys(phone)
        self.element_is_visible(LsLocators.email).send_keys(email)
        self.element_is_inv(LsLocators.block)
        self.element_is_visible(LsLocators.buy_checkbox).click()
        self.element_is_clickable(LsLocators.buy).click()

    @allure.step('Check tinkoff transaction')
    def check_tinkoff(self, text):
        title = self.element_is_visible(LsLocators.check_tinkoff).text
        assert title == text

    @allure.step('Check error messages')
    def error_messages(self, first_name, second_name, city, address, postcode, phone, email, text):
        self.element_is_visible(LsLocators.forward).click()
        self.element_is_inv(LsLocators.block)
        self.element_is_clickable(LsLocators.buy).click()
        error_first_name = self.element_is_visible(LsLocators.error_first_name).text
        error_second_name = self.element_is_visible(LsLocators.error_second_name).text
        error_city = self.element_is_visible(LsLocators.error_city).text
        error_address = self.element_is_visible(LsLocators.error_adress).text
        error_post_code = self.element_is_visible(LsLocators.error_post_code).text
        error_phone = self.element_is_visible(LsLocators.error_phone).text
        error_email = self.element_is_visible(LsLocators.error_email).text
        error_info = self.element_is_visible(LsLocators.error_info).text
        assert error_first_name == first_name
        assert error_second_name == second_name
        assert error_city == city
        assert error_address == address
        assert error_post_code == postcode
        assert error_phone == phone
        assert error_email == email
        assert error_info == text

    @allure.step('Check email')
    def check_email(self, text_email):
        alert = self.element_is_visible(LsLocators.email_alert)
        assert alert.text == text_email

    @allure.step('Check phone number')
    def check_phone(self, text_phone):
        alert = self.element_is_visible(LsLocators.phone_alert)
        assert alert.text == text_phone
