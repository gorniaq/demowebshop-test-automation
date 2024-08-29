import pytest
import allure
from hamcrest import assert_that, less_than_or_equal_to, greater_than_or_equal_to

from config.config import BOOKS_URL
from locators.books_page_locators import BooksPageLocators
from utils.browser_utils import BrowserUtils


class TestPageSize(BrowserUtils):

    @staticmethod
    def _verify_item_count(actual_count, expected_count):
        """
        Verify that the number of items displayed on the page matches the expected count.
        """
        if expected_count == 4:
            # Assert that the actual count is less than or equal to 4.
            assert_that(actual_count, less_than_or_equal_to(4),
                        "Incorrect number of items displayed (should be up to 4)")
        elif expected_count == 8:
            if actual_count < 5:
                # Assert that the actual count is less than or equal to the expected count.
                assert_that(actual_count, less_than_or_equal_to(expected_count),
                            "Incorrect number of items displayed (less than expected)")
            else:
                # Assert that the actual count is between 5 and 8.
                assert_that(actual_count, greater_than_or_equal_to(5),
                            "Incorrect number of items displayed (should be between 5 and 8)")
                assert_that(actual_count, less_than_or_equal_to(8),
                            "Incorrect number of items displayed (should be between 5 and 8)")
        elif expected_count == 12:
            if actual_count < 9:
                # Assert that the actual count is less than or equal to the expected count.
                assert_that(actual_count, less_than_or_equal_to(expected_count),
                            "Incorrect number of items displayed (less than expected)")
            else:
                # Assert that the actual count is greater than or equal to 9.
                assert_that(actual_count, greater_than_or_equal_to(9),
                            "Incorrect number of items displayed (should be more than 9)")

    @allure.feature('Books page')
    @allure.story('Verify that allows changing number of items on page')
    @pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
    def test_page_size(self, driver):
        # Use the utility to open the login URL
        with allure.step("Open URL"):
            self.open_url(driver, BOOKS_URL)

        with allure.step("Locate and click on the page size dropdown"):
            page_size_dropdown = self.wait_for_element(driver, BooksPageLocators.PAGE_SIZE_DROPDOWN, 20)
            page_size_dropdown.click()

        # List of page size options to be tested
        options = [
            BooksPageLocators.PAGE_SIZE_OPTION_4,
            BooksPageLocators.PAGE_SIZE_OPTION_8,
            BooksPageLocators.PAGE_SIZE_OPTION_12
        ]

        for option_locator in options:
            with allure.step(f"Click on the page size option locator: {option_locator}"):
                expected_count = self.select_dropdown_option_by_number(driver, option_locator)
                actual_count = self.get_actual_products_count(driver, BooksPageLocators.PRODUCT_TITLES)
                self._verify_item_count(actual_count, expected_count)
