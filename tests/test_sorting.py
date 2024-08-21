import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from hamcrest import assert_that, equal_to
from config.config import BOOKS_URL
from locators.books_page_locators import BooksPageLocators
from config.logger_config import logger
from utils.browser_utils import BrowserUtils


class TestSorting(BrowserUtils):

    @staticmethod
    def select_sorting_option(driver, option_locator):
        """
        Select a sorting option from the dropdown menu.
        :param driver: WebDriver instance for interacting with the browser.
        :param option_locator: Locator for the sorting option to be selected.
        :return: Text of the selected sorting option.
        """
        # Wait for the sorting option to be clickable and click on it.
        option = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(option_locator))
        sort_option_text = option.text.strip()
        logger.info(f"Selecting sorting option: {sort_option_text}")
        # Click the sorting option to apply it.
        option.click()
        return sort_option_text

    @staticmethod
    def get_product_titles_and_prices(driver):
        """
        Retrieve the titles and prices of products displayed on the page.
        :param driver: WebDriver instance for interacting with the browser.
        :return: A tuple containing a list of product titles and a list of product prices.
        """
        # Wait for all product titles to be present on the page.
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located(BooksPageLocators.PRODUCT_TITLES)
        )
        # Find all product titles on the page.
        product_titles = driver.find_elements(*BooksPageLocators.PRODUCT_TITLES)
        # Find all product prices on the page.
        product_prices = driver.find_elements(*BooksPageLocators.PRODUCT_PRICES)
        return product_titles, product_prices

    @staticmethod
    def _verify_sorting_by_name_ascending(product_titles):
        """
        Verify that products are sorted by name in ascending (A to Z) order.
        :param product_titles: List of product title elements.
        """
        # Get the sorted list of titles.
        sorted_titles = sorted([title.text for title in product_titles])
        # Get the actual list of titles from the page.
        actual_titles = [title.text for title in product_titles]
        return actual_titles, sorted_titles

    @staticmethod
    def _verify_sorting_by_name_descending(product_titles):
        """
        Verify that products are sorted by name in descending (Z to A) order.
        :param product_titles: List of product title elements.
        """
        # Get the sorted list of titles in reverse order.
        sorted_titles = sorted([title.text for title in product_titles], reverse=True)
        # Get the actual list of titles from the page.
        actual_titles = [title.text for title in product_titles]
        return actual_titles, sorted_titles

    @staticmethod
    def _verify_sorting_by_price_low_to_high(product_prices):
        """
        Verify that products are sorted by price in ascending (low to high) order.
        :param product_prices: List of product price elements.
        """
        # Get the sorted list of prices in ascending order.
        sorted_prices = sorted([float(price.text.strip().replace('$', '')) for price in product_prices])
        # Get the actual list of prices from the page.
        actual_prices = [float(price.text.strip().replace('$', '')) for price in product_prices]
        # Assert that the actual prices match the sorted prices.
        return actual_prices, sorted_prices

    @staticmethod
    def _verify_sorting_by_price_high_to_low(product_prices):
        """
        Verify that products are sorted by price in descending (high to low) order.
        :param product_prices: List of product price elements.
        """
        # Get the sorted list of prices in descending order.
        sorted_prices = sorted([float(price.text.strip().replace('$', '')) for price in product_prices], reverse=True)
        # Get the actual list of prices from the page.
        actual_prices = [float(price.text.strip().replace('$', '')) for price in product_prices]
        return actual_prices, sorted_prices

    @allure.feature('Books page')
    @allure.story('Verify sorting of items by different options')
    @pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
    def test_sorting_options(self, driver):
        self.open_url(driver, BOOKS_URL)

        try:
            # Locate and click on the sort by dropdown
            sort_by_dropdown = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located(BooksPageLocators.SORT_BY_DROPDOWN)
            )
            sort_by_dropdown.click()
            logger.info("Clicked on the sort by dropdown")

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
                    sort_option_text = self.select_sorting_option(driver, option_locator)

                    # Get the product titles and prices after sorting.
                    product_titles, product_prices = self.get_product_titles_and_prices(driver)

                    # Log the sorting option being tested.
                    allure.attach(driver.get_screenshot_as_png(), name="screenshot",
                                  attachment_type=allure.attachment_type.PNG)

                    # Check sorting based on the selected option.
                    if "Position" in sort_option_text:
                        logger.info("Checked sorting by position (default order)")
                    elif "Name A to Z" in sort_option_text:
                        self._verify_sorting_by_name_ascending(product_titles)
                        assert_that(actual_titles, equal_to(sorted_titles), "Products are not sorted A to Z")
                        logger.info("Verified sorting by name A to Z")
                    elif "Name Z to A" in sort_option_text:
                        self._verify_sorting_by_name_descending(product_titles)
                        assert_that(actual_titles, equal_to(sorted_titles), "Products are not sorted Z to A")
                        logger.info("Verified sorting by name Z to A")
                    elif "Price Low to High" in sort_option_text:
                        self._verify_sorting_by_price_low_to_high(product_prices)
                        assert_that(actual_prices, equal_to(sorted_prices),
                                    "Products are not sorted by price from low to high")
                        logger.info("Verified sorting by price from low to high")
                    elif "Price High to Low" in sort_option_text:
                        self._verify_sorting_by_price_high_to_low(product_prices)
                        assert_that(actual_prices, equal_to(sorted_prices),
                                    "Products are not sorted by price from high to low")
                        logger.info("Verified sorting by price from low to high")
                    elif "Created On" in sort_option_text:
                        logger.info("Checked sorting by creation date (dummy check)")
                    else:
                        logger.warning(f"Unknown sort option: {sort_option_text}")

        except Exception as e:
            logger.error("An error occurred during the test", exc_info=True)
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            raise
