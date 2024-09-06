from hamcrest import assert_that, less_than_or_equal_to, greater_than_or_equal_to

from locators.books_page_locators import BooksPageLocators
from utils.browser_utils import BrowserUtils


class PageSizeMethods:

    @staticmethod
    def open_books_page(driver, url):
        """Open the books page URL."""
        BrowserUtils.open_url(driver, url)

    @staticmethod
    def click_page_size_dropdown(driver):
        """Click on the page size dropdown."""
        page_size_dropdown = BrowserUtils.wait_for_element(driver, BooksPageLocators.PAGE_SIZE_DROPDOWN)
        page_size_dropdown.click()

    @staticmethod
    def select_page_size_option(driver, option_locator):
        """Select the page size option from the dropdown."""
        return BrowserUtils.select_dropdown_option_by_number(driver, option_locator)

    @staticmethod
    def verify_item_count(actual_count, expected_count):
        """Verify that the number of items displayed matches the expected count."""
        if expected_count == 4:
            assert_that(actual_count, less_than_or_equal_to(4),
                        "Incorrect number of items displayed (should be up to 4)")
        elif expected_count == 8:
            if actual_count < 5:
                assert_that(actual_count, less_than_or_equal_to(expected_count),
                            "Incorrect number of items displayed (less than expected)")
            else:
                assert_that(actual_count, greater_than_or_equal_to(5),
                            "Incorrect number of items displayed (should be between 5 and 8)")
                assert_that(actual_count, less_than_or_equal_to(8),
                            "Incorrect number of items displayed (should be between 5 and 8)")
        elif expected_count == 12:
            if actual_count < 9:
                assert_that(actual_count, less_than_or_equal_to(expected_count),
                            "Incorrect number of items displayed (less than expected)")
            else:
                assert_that(actual_count, greater_than_or_equal_to(9),
                            "Incorrect number of items displayed (should be more than 9)")
