from pages.base_page import BasePage
from pages.locators.main_locators import MainEvent
from selenium.webdriver.common.keys import Keys
import allure


class Accessories(BasePage):
    page_url = 'shop'

    @allure.step('Go to second katalog')
    def accessories(self):
        self.element_is_visible(MainEvent.second_katalog).click()

    @allure.step('Check title')
    def check_title(self, text):
        title = self.element_is_visible(MainEvent.hero_title)
        assert title.text == text

    @allure.step('Check full path')
    def check_full_path(self, text):
        full_path = self.element_is_visible(MainEvent.full_path_category)
        assert full_path.text == text

    @allure.step('Clear filters')
    def clear_filters(self):
        self.element_is_visible(MainEvent.filters).click()
        self.element_is_visible(MainEvent.button_filter).click()
        self.element_is_visible(MainEvent.clear_filters).click()

    @allure.step('Use all filters')
    def filters(self, first_input, second_input):
        self.element_is_visible(MainEvent.filters).click()
        self.element_is_visible(MainEvent.category_filter).click()
        self.element_is_visible(MainEvent.first_input).send_keys(first_input)
        self.element_is_visible(MainEvent.first_input).send_keys(Keys.ENTER)
        self.element_is_visible(MainEvent.electronic_category).click()
        self.element_is_visible(MainEvent.second_input).send_keys(second_input)
        self.element_is_visible(MainEvent.second_input).send_keys(Keys.ENTER)
        self.element_is_visible(MainEvent.button_filter).click()

    @allure.step('Check alert info')
    def no_items(self, text):
        title = self.element_is_visible(MainEvent.commerce_info)
        assert title.text == text

    @allure.step('Reset filters')
    def reset_filters(self):
        self.element_is_visible(MainEvent.reset).click()

    @allure.step('Search item')
    def search_item(self, input):
        self.element_is_visible(MainEvent.search_filter).send_keys(input)
        self.element_is_visible(MainEvent.button_search).click()

    @allure.step('English localization')
    def english(self):
        self.element_is_visible(MainEvent.english).click()
