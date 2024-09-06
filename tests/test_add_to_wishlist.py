import allure
from hamcrest import assert_that, contains_string, equal_to

from locators.wishlist_page_locators import WishlistPageLocators
from utils.auth_utils import AuthUtils
from config.config import WISHLIST_URL, BASE_URL
from utils.browser_utils import BrowserUtils
from utils.cart_and_wishlist_utils import CartAndWishlistUtils as cart_and_wishlist
from methods.wishlist_page_methods import WishlistPageMethods as wishlist_methods


class TestAddToWishlist(BrowserUtils):

    @allure.feature('Shopping Cart')
    @allure.story('Verify that a user can add an item to the cart')
    def test_add_to_wishlist(self, driver):
        # Open the login URL ang Log in to the application
        AuthUtils.login(driver)

        # Get the current cart quantity and clear the cart before starting the test
        with allure.step("Get the current wishlist quantity and clear the wishlist if necessary"):
            quantity_before = cart_and_wishlist.get_item_quantity(driver, WishlistPageLocators.WISHLIST_QTY)
            if int(quantity_before) != 0:
                cart_and_wishlist.clear(driver, WISHLIST_URL)
                self.open_url(driver, BASE_URL)

        # Find and click on the 'Apparel & Shoes' link
        with allure.step("Find and click on the 'Apparel & Shoes' link and add a product to the wishlist"):
            wishlist_methods.click_on_apparel_shoes_link(driver)
            # Find the first product item and navigate to page
            wishlist_methods.click_on_first_product(driver)
            # Add the product to the wishlist from the product page
            wishlist_methods.add_product_to_wishlist(driver)

        # Navigate to the wishlist page to verify the product is added
        with allure.step("Navigate to the wishlist page to verify the product is added"):
            product_name = self.get_product_title(driver, WishlistPageLocators.ITEM_TITLE)
            wishlist_methods.navigate_to_wishlist_page(driver)

        with allure.step("Verify that the product was added and the wishlist quantity increased by 1"):
            # Verify that the product is listed in the wishlist
            product_name_in_wishlist = self.get_product_title(driver, WishlistPageLocators.ITEM_NAME)
            assert_that(product_name, contains_string(product_name_in_wishlist))

            # Verify that the wishlist quantity increased by 1
            quantity_wishlist_page = self.get_element_attribute(driver, WishlistPageLocators.QUANTITY_INPUT, 'value')
            expected_quantity = int(quantity_before)

            assert_that(int(quantity_wishlist_page), equal_to(expected_quantity),
                        f"Wishlist quantity did not increase as expected. Expected: {expected_quantity}, "
                        f"Found: {int(quantity_wishlist_page)}")

            quantity_nav_link = cart_and_wishlist.get_item_quantity(driver, WishlistPageLocators.WISHLIST_QTY)

            assert_that(int(quantity_nav_link), equal_to(expected_quantity),
                        f"Wishlist quantity verification for the wishlist link failed. Expected: {expected_quantity},"
                        f" Found: {quantity_nav_link}")
