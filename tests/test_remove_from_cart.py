import pytest
import allure
from hamcrest import assert_that, equal_to

from config.config import CART_URL, BOOKS_URL
from locators.books_page_locators import BooksPageLocators
from utils.auth_utils import AuthUtils
from utils.browser_utils import BrowserUtils
from utils.cart_and_wishlist_utils import CartAndWishlistUtils


class TestRemoveFromCart(BrowserUtils, CartAndWishlistUtils):
    @allure.feature('Shopping Cart')
    @allure.story('Verify that a user can remove an item from the cart')
    @pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
    def test_remove_from_cart(self, driver):
        # Open the login URL and log in to the application
        with allure.step("Log in to the application"):
            AuthUtils.login(driver)

        # Navigate to the books page
        with allure.step("Navigate to the products page"):
            self.open_url(driver, BOOKS_URL)

        # Get the current cart quantity before adding a new item
        with allure.step("Get the current cart quantity"):
            quantity_before = CartAndWishlistUtils.get_item_quantity(driver, BooksPageLocators.CART_QUANTITY)

            # If the cart is empty, add a product to the cart
            if quantity_before == 0:
                self.add_product(driver, BooksPageLocators.ADD_TO_CART)
                # Verify that the product was added
                quantity_after_adding = CartAndWishlistUtils.get_item_quantity(driver, BooksPageLocators.CART_QUANTITY)
                assert_that(quantity_after_adding, equal_to(1),
                            f"Expected cart quantity to be 1 after adding a product, but found {quantity_after_adding}")

        # Navigate to the cart page
        with allure.step("Navigate to the cart page"):
            self.scroll_to_top(driver)
            self.wait_for_element_to_be_clickable(driver, BooksPageLocators.CART_LINK, 20)

        # Clear the cart using CartAndWishlistUtils
        with allure.step("Clear the cart"):
            self.clear(driver, CART_URL)
            quantity_after_clearing = CartAndWishlistUtils.get_item_quantity(driver, BooksPageLocators.CART_QUANTITY)
            assert_that(quantity_after_clearing, equal_to(0),
                        f"Expected cart quantity to be 0 after clearing the cart, but found {quantity_after_clearing}")
