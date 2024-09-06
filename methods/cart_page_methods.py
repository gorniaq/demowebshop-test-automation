from hamcrest import assert_that, equal_to

from locators.cart_page_locators import CartPageLocators
from utils.browser_utils import BrowserUtils
from utils.cart_and_wishlist_utils import CartAndWishlistUtils as cart_utils


class CartMethods:
    @staticmethod
    def clear_cart_if_not_empty(driver, cart_url, cart_quantity_locator):
        """Clear the cart if it is not empty."""
        quantity_before = cart_utils.get_item_quantity(driver, cart_quantity_locator)
        if int(quantity_before) != 0:
            cart_utils.clear(driver, cart_url)
        return quantity_before

    @staticmethod
    def verify_cart_quantity(driver, expected_quantity):
        """Verify that the cart quantity increased to the expected value."""
        quantity_cart_page = BrowserUtils.get_element_attribute(driver, CartPageLocators.QUANTITY_IN_CART, 'value')
        quantity_nav_link = cart_utils.get_item_quantity(driver, CartPageLocators.CART_QUANTITY)
        assert_that(int(quantity_cart_page), equal_to(expected_quantity),
                    f"Cart quantity {quantity_cart_page} did not increase as expected: {expected_quantity}.")
        assert_that(int(quantity_nav_link), equal_to(expected_quantity),
                    f"Cart quantity in nav link {quantity_nav_link} did not increase as expected: {expected_quantity}.")
