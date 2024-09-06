import allure
from hamcrest import assert_that, contains_string, equal_to

from locators.cart_page_locators import CartPageLocators
from utils.auth_utils import AuthUtils
from locators.books_page_locators import BooksPageLocators
from config.config import BOOKS_URL, CART_URL
from utils.browser_utils import BrowserUtils
from utils.cart_and_wishlist_utils import CartAndWishlistUtils as cart_and_wishlist
from methods.cart_page_methods import CartMethods as cart_methods


class TestAddToCart(BrowserUtils):

    @allure.feature('Shopping Cart')
    @allure.story('Verify that a user can add an item to the cart')
    def test_add_to_cart(self, driver):
        # Open the login URL ang Log in to the application
        AuthUtils.login(driver)

        with allure.step("Clear the cart if is not empty"):
            cart_methods.clear_cart_if_not_empty(driver, CART_URL, CartPageLocators.CART_QUANTITY)

        # Navigate to the books page
        with allure.step("Navigate to the product page and add the product to the cart"):
            self.open_url(driver, BOOKS_URL)
            # Get the name of the first product listed on the books page
            product_name = self.get_product_title(driver, BooksPageLocators.ITEM_NAME)
            cart_and_wishlist.add_product(driver, BooksPageLocators.ADD_TO_CART)

        #  Navigate to the product page and add product to the cart
        with allure.step("Add the product to the cart from the product page"):
            # Scroll to the product link element to ensure it's visible and clickable
            self.scroll_to_element(driver, BooksPageLocators.ITEM_PRODUCT)
            self.wait_for_element_and_click(driver, BooksPageLocators.ITEM_PRODUCT)
            cart_and_wishlist.add_product(driver, BooksPageLocators.FIRST_ITEM_ADD_TO_CART)

        # Navigate to the cart page to verify the product is added
        with allure.step("Click on the 'Shopping cart' link to navigate to the cart page"):
            self.scroll_to_top(driver)
            self.wait_for_element_and_click(driver, BooksPageLocators.CART_LINK)

        # Get the product name in the cart and verify it matches the product added
        with allure.step("Get the product name in cart"):
            product_name_in_cart = self.get_product_title(driver, CartPageLocators.ITEM_NAME)
            assert_that(product_name, contains_string(product_name_in_cart),
                        f"Product name in cart: {product_name_in_cart} does not match the expected name: {product_name}.")

        # Verify that the cart quantity increased by 2
        with allure.step("Verify that the cart quantity increased by 2"):
            # Get the cart quantity from the input field on the Cart Page
            cart_methods.verify_cart_quantity(driver, 2)
