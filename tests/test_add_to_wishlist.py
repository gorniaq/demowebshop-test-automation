import pytest
import allure
from hamcrest import assert_that, contains_string, equal_to
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.logger_config import logger
from locators.wishlist_page_locators import WishlistPageLocators
from utils.auth_utils import AuthUtils
from config.config import WISHLIST_URL, BASE_URL
from utils.browser_utils import BrowserUtils
from utils.cart_and_wishlist_utils import CartAndWishlistUtils


class TestAddToWishlist(AuthUtils, BrowserUtils, CartAndWishlistUtils):

    @allure.feature('Shopping Cart')
    @allure.story('Verify that a user can add an item to the cart')
    @pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
    def test_add_to_wishlist(self, driver):
        # Open the login URL ang Log in to the application
        self.login(driver)
        logger.info("Logged in successfully")

        try:
            # Get the current cart quantity before adding a new item
            with allure.step("Get the current cart quantity"):
                quantity_before = self.get_items_quantity(driver, WishlistPageLocators.WISHLIST_QTY)
                logger.info(f"Initial cart quantity: {quantity_before}")

            # Clear the cart before starting the test
            with allure.step("Clear the cart if not empty"):
                if int(quantity_before) != 0:
                    logger.info("Cart is not empty, clearing the cart")
                    self.clear(driver, WISHLIST_URL)
                    BrowserUtils.open_url(driver, BASE_URL)
                else:
                    logger.info("Cart is already empty")

            # Find and click on the 'Apparel & Shoes' link
            with allure.step("Find and click on 'Apparel & Shoes' link"):
                self.open_url(driver, BASE_URL)
                apparel_shoes_link = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(WishlistPageLocators.APPAREL_SHOES_LINK)
                )
                apparel_shoes_link.click()

            # Find the first product item and navigate to page
            with allure.step("Click on the first product item"):
                product_item = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(WishlistPageLocators.PRODUCT_ITEM)
                )
                product_item.click()

            # Add the product to the wishlist from the product page
            with allure.step("Click on the 'Add to wishlist' button for the product"):
                self.add_product(driver, WishlistPageLocators.ADD_TO_WISHLIST_BUTTON)
                logger.info(f"Clicked 'Add to wishlist' for product: {WishlistPageLocators.PRODUCT_ITEM}")

            # Navigate to the wishlist page to verify the product is added
            with allure.step("Click on the 'Wishlist' link to navigate to the wishlist page"):
                product_name = self.get_product_name(driver, WishlistPageLocators.ITEM_TITLE)
                logger.info(f"Product name retrieved: {product_name}")
                BrowserUtils.scroll_to_top(driver)
                logger.info("Scrolled to the top of the page")
                wishlist_link = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(WishlistPageLocators.WISHLIST_NAV_LINK)
                )
                wishlist_link.click()

            # Verify that the product is listed in the wishlist
            with allure.step("Get the product name in Wishlist"):
                product_name_in_wishlist = self.get_product_name(driver, WishlistPageLocators.ITEM_NAME)
                logger.info(f"Product name wishlist: {product_name_in_wishlist}")
                assert_that(product_name, contains_string(product_name_in_wishlist))
                logger.info("Product name verification passed")

            # Verify that the wishlist quantity increased by 1
            with allure.step("Verify that the wishlist quantity increased by 1"):
                # Get the wishlist quantity from the input field on the Wishlist Page
                quantity_wishlist_page = self.get_element_attribute(driver, WishlistPageLocators.QUANTITY_INPUT, 'value')
                expected_quantity = int(quantity_before)
                logger.info(f"Wishlist quantity after adding products: {quantity_wishlist_page} Expected: {expected_quantity}, Found: {quantity_wishlist_page}")

                assert_that(int(quantity_wishlist_page), equal_to(expected_quantity),
                            "Wishlist quantity did not increase as expected.")

                quantity_nav_link = self.get_items_quantity(driver, WishlistPageLocators.WISHLIST_QTY)

                logger.info(f"Wishlist quantity verification for the wishlist link passed. Expected: {expected_quantity}, Found: {quantity_nav_link}")

                assert_that(int(quantity_nav_link), equal_to(expected_quantity),
                            "Wishlist quantity did not increase as expected.")

        except Exception as e:
            logger.error(f"Test failed due to {str(e)}")
            allure.attach(driver.get_screenshot_as_png(), name="add_to_cart_failure_screenshot",
                          attachment_type=allure.attachment_type.PNG)
            raise
