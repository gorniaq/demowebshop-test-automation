import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from hamcrest import assert_that, equal_to
from config.config import CART_URL, BOOKS_URL
from config.logger_config import logger
from locators.books_page_locators import BooksPageLocators
from utils.auth_utils import AuthUtils
from utils.browser_utils import BrowserUtils
from utils.cart_and_wishlist_utils import CartAndWishlistUtils


class TestRemoveFromCart(BrowserUtils, AuthUtils, CartAndWishlistUtils):
    @allure.feature('Shopping Cart')
    @allure.story('Verify that a user can remove an item from the cart')
    @pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
    def test_remove_from_cart(self, driver):
        # Open the login URL and log in to the application
        self.login(driver)
        logger.info("Logged in successfully")

        try:
            # Navigate to the books page
            with allure.step("Navigate to the products page"):
                self.open_url(driver, BOOKS_URL)

            # Get the current cart quantity before adding a new item
            with allure.step("Get the current cart quantity"):
                quantity_before = CartAndWishlistUtils.get_items_quantity(driver, BooksPageLocators.CART_QUANTITY)
                logger.info(f"Initial cart quantity: {quantity_before}")

            # # If the cart is empty, add a product to the cart
            if quantity_before == 0:
                with allure.step("Cart is empty, adding a product to the cart"):
                    self.add_product(driver, BooksPageLocators.ADD_TO_CART)
                    # Verify that the product was added
                    quantity_after_adding = CartAndWishlistUtils.get_items_quantity(driver, BooksPageLocators.CART_QUANTITY)
                    assert_that(quantity_after_adding, equal_to(1))

            # Navigate to the cart page
            with allure.step("Navigate to the cart page"):
                BrowserUtils.scroll_to_top(driver)
                cart_link = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(BooksPageLocators.CART_LINK)
                )
                cart_link.click()
                logger.info("Navigated to the cart page")

            # Clear the cart using CartAndWishlistUtils
            with allure.step("Clear the cart"):
                self.clear(driver, CART_URL)
                quantity_after_clearing = CartAndWishlistUtils.get_items_quantity(driver, BooksPageLocators.CART_QUANTITY)
                assert_that(quantity_after_clearing, equal_to(0))

        except Exception as e:
            logger.error(f"Test failed due to {str(e)}")
            allure.attach(driver.get_screenshot_as_png(), name="remove_from_cart_failure_screenshot",
                          attachment_type=allure.attachment_type.PNG)
            raise
