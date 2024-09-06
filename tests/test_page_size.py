import allure

from config.config import BOOKS_URL
from constants import OPTIONS_PAGE_SIZE
from locators.books_page_locators import BooksPageLocators
from utils.browser_utils import BrowserUtils
from methods.page_size_methods import PageSizeMethods as page_size_methods


class TestPageSize(BrowserUtils):

    @allure.feature('Books page')
    @allure.story('Verify that allows changing number of items on page')
    def test_page_size(self, driver):
        # Use the utility to open the URL
        self.open_url(driver, BOOKS_URL)

        with allure.step("Locate and click on the page size dropdown"):
            page_size_dropdown = self.wait_for_element(driver, BooksPageLocators.PAGE_SIZE_DROPDOWN)
            page_size_dropdown.click()

        for option_locator in OPTIONS_PAGE_SIZE:
            with allure.step(f"Click on the page size option locator: {option_locator}"):
                expected_count = self.select_dropdown_option_by_number(driver, option_locator)
                actual_count = self.get_actual_products_count(driver, BooksPageLocators.PRODUCT_TITLES)
                page_size_methods.verify_item_count(actual_count, expected_count)
