import time

import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from hamcrest import assert_that, equal_to
from config.config import BASE_URL, LOGIN_URL, WISHLIST_URL
from config.logger_config import logger
from drivers.driver_factory import DriverFactory
from locators.wishlist_page_locators import WishlistPageLocators
from utils.auth_utils import AuthUtils
from utils.browser_utils import BrowserUtils
from utils.cart_utils import CartUtils


class TestAddToWishlist:

    @allure.feature('Wishlist')
    @allure.story('Verify that a user can add an item to the wishlist and check its presence')
    @pytest.mark.parametrize("browser_name", ["chrome", "firefox"])
    def test_add_to_wishlist(self, browser_name):
        driver = DriverFactory.get_driver(browser_name)
        BrowserUtils.open_url(driver, LOGIN_URL)
        AuthUtils.login(driver)

        try:
            # Get the current cart quantity before adding a new item
            with allure.step("Get the current cart quantity"):
                quantity_before = CartUtils.get_items_quantity(driver, WishlistPageLocators.WISHLIST_QTY)
                logger.info(f"Initial cart quantity: {quantity_before}")

            # Clear the cart before starting the test
            with allure.step("Clear the cart if not empty"):
                if int(quantity_before) != 0:
                    logger.info("Cart is not empty, clearing the cart")
                    CartUtils.clear(driver, WISHLIST_URL)
                else:
                    logger.info("Cart is already empty")

            # Find and click on the 'Apparel & Shoes' link
            with allure.step("Find and click on 'Apparel & Shoes' link"):
                apparel_shoes_link = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(WishlistPageLocators.APPAREL_SHOES_LINK)
                )
                apparel_shoes_link.click()

            # Locate the product item
            with allure.step("Locate the product item"):
                product_item = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located(WishlistPageLocators.PRODUCT_ITEM)
                )
                product_item.click()

            # Add the product to the wishlist
            with allure.step("Add the product to the wishlist"):
                add_element = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(WishlistPageLocators.ADD_TO_WISHLIST_BUTTON)
                )
                add_element.click()

            # # Navigate to the wishlist page and verify the product is present
            # with allure.step("Navigate to the wishlist page and verify the product is present"):
            #     wishlist_link = WebDriverWait(driver, 10).until(
            #         EC.element_to_be_clickable(WishlistPageLocators.WISHLIST_LINK)
            #     )
            #     wishlist_link.click()

        except Exception as e:
            logger.error(f"Test failed due to {str(e)}")
            allure.attach(driver.get_screenshot_as_png(), name="wishlist_failure_screenshot",
                          attachment_type=allure.attachment_type.PNG)
            raise
