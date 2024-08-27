import pytest
import allure
from hamcrest import assert_that, contains_string, equal_to
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.logger_config import logger
from locators.cart_page_locators import CartPageLocators
from utils.auth_utils import AuthUtils
from locators.books_page_locators import BooksPageLocators
from config.config import BOOKS_URL, CART_URL
from utils.browser_utils import BrowserUtils
from utils.cart_and_wishlist_utils import CartAndWishlistUtils


class TestAddToCart(AuthUtils, CartAndWishlistUtils, BrowserUtils):

    @allure.feature('Shopping Cart')
    @allure.story('Verify that a user can add an item to the cart')
    @pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
    def test_add_to_cart(self, driver):
        # Open the login URL ang Log in to the application
        self.login(driver)
        logger.info("Logged in successfully")

        try:
            # Get the current cart quantity before adding a new item
            with allure.step("Get the current cart quantity"):
                quantity_before = self.get_items_quantity(driver, CartPageLocators.CART_QUANTITY)
                logger.info(f"Initial cart quantity: {quantity_before}")

            # Clear the cart before starting the test
            with allure.step("Clear the cart if not empty"):
                if int(quantity_before) != 0:
                    logger.info("Cart is not empty, clearing the cart")
                    self.clear(driver, CART_URL)
                else:
                    logger.info("Cart is already empty")

            # Navigate to the books page
            with allure.step("Navigate to the products page"):
                self.open_url(driver, BOOKS_URL)
                logger.info("Navigated to the books page")

            # Get the name of the first product listed on the books page
            with allure.step("Get the product name"):
                product_name = self.get_product_name(driver, BooksPageLocators.ITEM_NAME)
                logger.info(f"Product name retrieved: {product_name}")

            # Navigate to the product page by clicking on the product link
            with allure.step("Click on the 'Add to cart' button for the product"):
                self.add_product(driver, BooksPageLocators.ADD_TO_CART)
                logger.info(f"Clicked 'Add to cart' for product: {product_name}")

            # with allure.step("Wait for notification to appear"):
            #     # Wait until the notification element is visible on the page
            #     WebDriverWait(driver, 10).until(
            #         EC.visibility_of_element_located(BooksPageLocators.NOTIFICATION)
            #     )
            #     # Retrieve the text from the notification element
            #     notification_text = NotificationHandler.get_notification_text(driver).strip()
            #     # Log the notification text received
            #     logger.info(f"Notification text received: '{notification_text}'")
            #     # Verify that the notification text contains the expected success message
            #     assert_that(notification_text, contains_string(ADD_TO_CART_SUCCESS_MESSAGE),
            #                 "Notification text does not match expected value.")

            # Navigate to the product page by clicking on the product link
            with allure.step("Click and navigate to product page"):
                # Scroll to the product link element to ensure it's visible and clickable
                self.scroll_to_element(driver, BooksPageLocators.ITEM_PRODUCT)
                logger.info("Navigated to the product page")
                # Click on the product link to navigate to the product page
                product_link = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(BooksPageLocators.ITEM_PRODUCT)
                )
                product_link.click()
                logger.info("Navigated to the product page")

            # Add the product to the cart from the product page
            with allure.step("Click on the 'Add to cart' button for the product"):
                self.add_product(driver, BooksPageLocators.FIRST_ITEM_ADD_TO_CART)
                logger.info("Clicked 'Add to cart' from the product page")

            # Navigate to the cart page to verify the product is added
            with allure.step("Click on the 'Shopping cart' link to navigate to the cart page"):
                self.scroll_to_top(driver)
                logger.info("Scrolled to the top of the page")
                cart_link = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(BooksPageLocators.CART_LINK)
                )
                cart_link.click()

            # Get the product name in the cart and verify it matches the product added
            with allure.step("Get the product name in cart"):
                product_name_in_cart = self.get_product_name(driver, CartPageLocators.ITEM_NAME)
                logger.info(f"Product name in cart: {product_name_in_cart}")
                assert_that(product_name, contains_string(product_name_in_cart))
                logger.info("Product name verification passed")

            # Verify that the cart quantity increased by 2
            with allure.step("Verify that the cart quantity increased by 2"):
                # Get the cart quantity from the input field on the Cart Page
                quantity_cart_page = self.get_element_attribute(driver, CartPageLocators.QUANTITY_IN_CART, 'value')
                logger.info(f"Cart quantity after adding products: {quantity_cart_page}")

                quantity_nav_link = CartAndWishlistUtils.get_items_quantity(driver,  CartPageLocators.CART_QUANTITY)

                expected_quantity = int(quantity_before)
                assert_that(int(quantity_cart_page), equal_to(expected_quantity),
                            "Cart quantity did not increase as expected.")

                logger.info(
                    f"Cart quantity verification on the cart page passed.. Expected: {expected_quantity}, Found: {quantity_cart_page}")

                assert_that(int(quantity_nav_link), equal_to(expected_quantity),
                            "Cart quantity did not increase as expected.")
                logger.info(
                    f"Cart quantity verification for the cart link passed. Expected: {expected_quantity}, Found: {quantity_nav_link}")

        except Exception as e:
            logger.error(f"Test failed due to {str(e)}")
            allure.attach(driver.get_screenshot_as_png(), name="add_to_cart_failure_screenshot",
                          attachment_type=allure.attachment_type.PNG)
            raise
