from locators.wishlist_page_locators import WishlistPageLocators
from utils.browser_utils import BrowserUtils


class WishlistPageMethods:

    @staticmethod
    def click_on_apparel_shoes_link(driver, timeout=20):
        """Click on the 'Apparel & Shoes' link."""
        BrowserUtils.wait_for_element_and_click(driver, WishlistPageLocators.APPAREL_SHOES_LINK, timeout)

    @staticmethod
    def click_on_first_product(driver, timeout=20):
        """Click on the first product listed on the page."""
        BrowserUtils.wait_for_element_and_click(driver, WishlistPageLocators.PRODUCT_ITEM, timeout)

    @staticmethod
    def add_product_to_wishlist(driver, timeout=20):
        """Add the product to the wishlist."""
        BrowserUtils.wait_for_element_and_click(driver, WishlistPageLocators.ADD_TO_WISHLIST_BUTTON, timeout)

    @staticmethod
    def navigate_to_wishlist_page(driver, timeout=20):
        """Navigate to the wishlist page."""
        BrowserUtils.scroll_to_top(driver)
        BrowserUtils.wait_for_element_and_click(driver, WishlistPageLocators.WISHLIST_NAV_LINK, timeout)

    @staticmethod
    def get_product_name_in_wishlist(driver):
        """Get the product name from the wishlist."""
        return BrowserUtils.get_product_title(driver, WishlistPageLocators.ITEM_NAME)
