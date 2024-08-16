import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from hamcrest import assert_that, less_than_or_equal_to, greater_than_or_equal_to
from config.logger_config import logger
from drivers.driver_factory import DriverFactory
from config.config import BOOKS_URL
from locators.books_page_locators import BooksPageLocators
from utils.browser_utils import BrowserUtils


class TestPageSize:

    @staticmethod
    def select_page_size_option(driver, option_locator):
        """
        Select the page size option by clicking on the dropdown item and return the expected count of items.
        :param driver: WebDriver instance for interacting with the browser.
        :param option_locator: Locator for the page size option to be selected.
        :return: Expected number of items that should be displayed on the page after selecting the option.
        """
        # Wait for the page size option to be clickable and click on it.
        option = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(option_locator))
        # Extract the number of items per page from the option text.
        expected_count = int(option.text.strip())
        # Log the selected page size option.
        logger.info("Selected page size option: %d", expected_count)
        # Click the option to apply the selected page size.
        option.click()
        return expected_count

    @staticmethod
    def get_actual_product_count(driver):
        """
        Retrieve the actual number of product titles currently displayed on the page.
        :param driver: WebDriver instance for interacting with the browser.
        :return: Actual count of items displayed on the page.
        """
        # Wait for all product titles to be present on the page.
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located(BooksPageLocators.PRODUCT_TITLES)
        )
        # Find all product titles on the page.
        product_titles = driver.find_elements(*BooksPageLocators.PRODUCT_TITLES)
        # Get the count of product titles.
        actual_count = len(product_titles)
        # Log the actual count of items displayed.
        logger.info("Actual count of items displayed: %d", actual_count)
        return actual_count

    @staticmethod
    def verify_item_count(actual_count, expected_count):
        """
        Verify that the number of items displayed on the page matches the expected count.
        :param actual_count: Actual number of items displayed on the page.
        :param expected_count: Expected number of items to be displayed on the page.
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
    @pytest.mark.parametrize("browser_name", ["chrome", "firefox"])
    def test_page_size(self, browser_name):
        # Initialize WebDriver for the specified browser and navigate to the Books page
        driver = DriverFactory.get_driver(browser_name)
        BrowserUtils.open_url(driver, BOOKS_URL)

        try:
            with allure.step("Locate and click on the page size dropdown"):
                page_size_dropdown = WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located(BooksPageLocators.PAGE_SIZE_DROPDOWN)
                )
                page_size_dropdown.click()

            # List of page size options to be tested
            options = [
                BooksPageLocators.PAGE_SIZE_OPTION_4,
                BooksPageLocators.PAGE_SIZE_OPTION_8,
                BooksPageLocators.PAGE_SIZE_OPTION_12
            ]

            for option_locator in options:
                with allure.step(f"Click on the page size option locator: {option_locator}"):
                    # Select the page size option and get the expected item count
                    expected_count = self.select_page_size_option(driver, option_locator)

                    # Get the actual number of items displayed after selecting the option
                    actual_count = self.get_actual_product_count(driver)

                    # Verify that the actual number of items matches the expected count
                    self.verify_item_count(actual_count, expected_count)

        except Exception as e:
            logger.error("An error occurred: %s", str(e))
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            raise
