import pytest
import allure
from hamcrest import assert_that, equal_to

from config.config import BOOKS_URL
from utils.auth_utils import AuthUtils
from utils.browser_utils import BrowserUtils
from utils.cart_and_wishlist_utils import CartAndWishlistUtils
from locators.books_page_locators import BooksPageLocators
from locators.checkout_page_locators import CheckoutPageLocators


class TestCheckout(AuthUtils, BrowserUtils):
    @allure.feature('Checkout')
    @allure.story('Verify that a user can checkout an item')
    @pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
    def test_checkout(self, driver):
        # Open the login URL ang Log in to the application
        with allure.step("Log in to the application"):
            AuthUtils.login(driver)

        # Check the current cart quantity
        with allure.step("Check cart quantity"):
            quantity = CartAndWishlistUtils.get_item_quantity(driver, BooksPageLocators.CART_QUANTITY)

            if quantity == 0:
                # If the cart is empty, navigate to the books page and add a product
                self.open_url(driver, BOOKS_URL)
                self.wait_for_element_and_click(driver, BooksPageLocators.ADD_TO_CART, 20)

        with allure.step("Verify the product was added to the cart"):
            # Verify the product was added
            quantity_after_adding = self.get_actual_products_count(driver, BooksPageLocators.CART_QUANTITY)
            assert_that(quantity_after_adding, equal_to(1),
                        f"Expected cart quantity to be 1 after adding a product, but found {quantity_after_adding}")

        # Navigate to the cart page
        with allure.step("Navigate to the cart page"):
            self.wait_for_element_and_click(driver, BooksPageLocators.CART_LINK, 20)

        # Agree to terms and proceed to checkout
        with allure.step("Agree to terms and proceed to checkout"):
            self.wait_for_element_and_click(driver, CheckoutPageLocators.TERMS_OF_SERVICE_CHECKBOX, 20)
            self.wait_for_element_and_click(driver, CheckoutPageLocators.CHECKOUT_BUTTON, 20)

        # Verify the checkout form is displayed
        with allure.step("Verify checkout steps form is displayed"):
            self.wait_for_element(driver,CheckoutPageLocators.CHECKOUT_STEPS_FORM, 20)
