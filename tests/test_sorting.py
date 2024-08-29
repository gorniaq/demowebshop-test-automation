import allure
from hamcrest import assert_that, equal_to

from config.config import BOOKS_URL
from locators.books_page_locators import BooksPageLocators
from config.logger_config import logger
from utils.sorting_utils import SortingUtils


class TestSorting(SortingUtils):

    @allure.feature('Books page')
    @allure.story('Verify sorting of items by different options')
    def test_sorting_options(self, driver):
        # Use the utility to open the login URL
        self.open_url(driver, BOOKS_URL)

        # Locate and click on the sort by dropdown
        self.wait_for_element_and_click(driver, BooksPageLocators.SORT_BY_DROPDOWN)

        # Define sorting options and their expected behaviors
        sorting_options = [
            BooksPageLocators.SORT_BY_POSITION,
            BooksPageLocators.SORT_BY_NAME_A_TO_Z,
            BooksPageLocators.SORT_BY_NAME_Z_TO_A,
            BooksPageLocators.SORT_BY_PRICE_LOW_TO_HIGH,
            BooksPageLocators.SORT_BY_PRICE_HIGH_TO_LOW,
            BooksPageLocators.SORT_BY_CREATED_ON
        ]

        for option_locator in sorting_options:
            with allure.step(f"Select and verify sorting option: {option_locator}"):
                # Select the sorting option and get its text.
                sort_option_text = self.select_dropdown_option_by_text(driver, option_locator)

                # Get the product titles and prices after sorting.
                product_titles, product_prices = self.get_product_titles_and_prices(driver)

                # Check sorting based on the selected option.
                if "Position" in sort_option_text:
                    logger.info("Checked sorting by position (default order)")
                elif "Name A to Z" in sort_option_text:
                    self.verify_sorting_by_name_ascending(product_titles)
                    assert_that(actual_titles, equal_to(sorted_titles), "Products are not sorted A to Z")
                elif "Name Z to A" in sort_option_text:
                    self.verify_sorting_by_name_descending(product_titles)
                    assert_that(actual_titles, equal_to(sorted_titles), "Products are not sorted Z to A")
                elif "Price Low to High" in sort_option_text:
                    self.verify_sorting_by_price_low_to_high(product_prices)
                    assert_that(actual_prices, equal_to(sorted_prices),
                                "Products are not sorted by price from low to high")
                elif "Price High to Low" in sort_option_text:
                    self.verify_sorting_by_price_high_to_low(product_prices)
                    assert_that(actual_prices, equal_to(sorted_prices),
                                "Products are not sorted by price from high to low")
