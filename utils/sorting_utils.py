from locators.books_page_locators import BooksPageLocators
from utils.browser_utils import BrowserUtils


class SortingUtils(BrowserUtils):

    @staticmethod
    def get_product_titles_and_prices(driver):
        # Find all product titles on the page.
        product_titles = BrowserUtils.get_elements(driver, BooksPageLocators.PRODUCT_TITLES)
        # Find all product prices on the page.
        product_prices = BrowserUtils.get_elements(driver, BooksPageLocators.PRODUCT_PRICES)

        return product_titles, product_prices

    @staticmethod
    def verify_sorting_by_name_ascending(product_titles):
        """
        Verify that products are sorted by name in ascending (A to Z) order.        """
        # Get the sorted list of titles.
        sorted_titles = sorted([title.text for title in product_titles])
        # Get the actual list of titles from the page.
        actual_titles = [title.text for title in product_titles]

        return actual_titles, sorted_titles

    @staticmethod
    def verify_sorting_by_name_descending(product_titles):
        """
        Verify that products are sorted by name in descending (Z to A) order.
        """
        # Get the sorted list of titles in reverse order.
        sorted_titles = sorted([title.text for title in product_titles], reverse=True)
        # Get the actual list of titles from the page.
        actual_titles = [title.text for title in product_titles]

        return actual_titles, sorted_titles

    @staticmethod
    def verify_sorting_by_price_low_to_high(product_prices):
        """
        Verify that products are sorted by price in ascending (low to high) order.
        """
        # Get the sorted list of prices in ascending order.
        sorted_prices = sorted([float(price.text.strip().replace('$', '')) for price in product_prices])
        # Get the actual list of prices from the page.
        actual_prices = [float(price.text.strip().replace('$', '')) for price in product_prices]

        return actual_prices, sorted_prices

    @staticmethod
    def verify_sorting_by_price_high_to_low(product_prices):
        """
        Verify that products are sorted by price in descending (high to low) order.
        """
        # Get the sorted list of prices in descending order.
        sorted_prices = sorted([float(price.text.strip().replace('$', '')) for price in product_prices], reverse=True)
        # Get the actual list of prices from the page.
        actual_prices = [float(price.text.strip().replace('$', '')) for price in product_prices]

        return actual_prices, sorted_prices
