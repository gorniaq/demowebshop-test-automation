import allure
from hamcrest import assert_that, contains_string, equal_to

from locators.cart_page_locators import CartPageLocators
from utils.auth_utils import AuthUtils
from locators.books_page_locators import BooksPageLocators
from config.config import BOOKS_URL, CART_URL
from utils.browser_utils import BrowserUtils
from utils.cart_and_wishlist_utils import CartAndWishlistUtils


class TestAddToCart(CartAndWishlistUtils, BrowserUtils):

    @allure.feature('Shopping Cart')
    @allure.story('Verify that a user can add an item to the cart')
    def test_add_to_cart(self, driver):
        # Open the login URL ang Log in to the application
        AuthUtils.login(driver)

        with allure.step("Clear the cart if is not empty"):
            # Get the current cart quantity before adding a new item
            quantity_before = self.get_item_quantity(driver, CartPageLocators.CART_QUANTITY)
            # Clear the cart before starting the test
            if int(quantity_before) != 0:
                self.clear(driver, CART_URL)

        # Navigate to the books page
        with allure.step("Navigate to the product page and add the product to the cart"):
            self.open_url(driver, BOOKS_URL)
            # Get the name of the first product listed on the books page
            product_name = self.get_product_title(driver, BooksPageLocators.ITEM_NAME)
            self.add_product(driver, BooksPageLocators.ADD_TO_CART)

        #  Navigate to the product page and add product to the cart
        with allure.step("Add the product to the cart from the product page"):
            # Scroll to the product link element to ensure it's visible and clickable
            self.scroll_to_element(driver, BooksPageLocators.ITEM_PRODUCT)
            self.wait_for_element_and_click(driver, BooksPageLocators.ITEM_PRODUCT)
            self.add_product(driver, BooksPageLocators.FIRST_ITEM_ADD_TO_CART)

        # Navigate to the cart page to verify the product is added
        with allure.step("Click on the 'Shopping cart' link to navigate to the cart page"):
            self.scroll_to_top(driver)
            self.wait_for_element_and_click(driver, BooksPageLocators.CART_LINK)

        # Get the product name in the cart and verify it matches the product added
        with allure.step("Get the product name in cart"):
            product_name_in_cart = self.get_product_title(driver, CartPageLocators.ITEM_NAME)
            assert_that(product_name, contains_string(product_name_in_cart),
                        f"Product name in cart: {product_name_in_cart} does not match the expected name: {product_name}")

        # Verify that the cart quantity increased by 2
        with allure.step("Verify that the cart quantity increased by 2"):
            # Get the cart quantity from the input field on the Cart Page
            quantity_cart_page = self.get_element_attribute(driver, CartPageLocators.QUANTITY_IN_CART, 'value')

            quantity_nav_link = CartAndWishlistUtils.get_item_quantity(driver,  CartPageLocators.CART_QUANTITY)

            assert_that(int(quantity_cart_page), equal_to(2),
                        f"Cart quantity {quantity_cart_page} did not increase as expected: 2.")

            assert_that(int(quantity_nav_link), equal_to(2),
                        f"Cart quantity in nav link {quantity_nav_link} did not increase as expected: 2.")
