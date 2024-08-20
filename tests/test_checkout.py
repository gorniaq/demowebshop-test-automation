import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from hamcrest import assert_that, equal_to
from config.config import BOOKS_URL, LOGIN_URL
from config.logger_config import logger
from drivers.driver_factory import DriverFactory
from utils.auth_utils import AuthUtils
from utils.browser_utils import BrowserUtils
from utils.cart_utils import CartUtils
from locators.books_page_locators import BooksPageLocators
from locators.checkout_page_locators import CheckoutPageLocators


class TestCheckout:
    @allure.feature('Checkout')
    @allure.story('Verify that a user can checkout an item')
    @pytest.mark.parametrize("browser_name", ["chrome", "firefox"])
    def test_checkout(self, browser_name):
        # Initialize the WebDriver for the specified browser
        driver = DriverFactory.get_driver(browser_name)
        logger.info(f"Initialized WebDriver for {browser_name}")

        # Open the login URL and log in to the application
        BrowserUtils.open_url(driver, LOGIN_URL)
        logger.info(f"Opened login URL: {LOGIN_URL}")
        AuthUtils.login(driver)
        logger.info("Logged in successfully")

        try:
            # Check the current cart quantity
            with allure.step("Check cart quantity"):
                quantity = CartUtils.get_items_quantity(driver, BooksPageLocators.CART_QUANTITY)
                logger.info(f"Current cart quantity: {quantity}")

                if quantity == 0:
                    # If the cart is empty, navigate to the books page and add a product
                    with allure.step("Cart is empty, navigating to the products page"):
                        BrowserUtils.open_url(driver, BOOKS_URL)
                        logger.info("Navigated to the books page to add a product.")

                    with allure.step("Add a product to the cart"):
                        add_to_cart_button = WebDriverWait(driver, 10).until(
                            EC.element_to_be_clickable(BooksPageLocators.ADD_TO_CART)
                        )
                        add_to_cart_button.click()
                        logger.info("Clicked 'Add to Cart' button.")

                    # Verify the product was added
                    quantity_after_adding = CartUtils.get_items_quantity(driver, BooksPageLocators.CART_QUANTITY)
                    assert_that(quantity_after_adding, equal_to(1))
                else:
                    # If the cart is not empty, proceed with the checkout process
                    logger.info("Cart is not empty. Proceeding to checkout.")

            # Navigate to the cart page
            with allure.step("Navigate to the cart page"):
                cart_link = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(BooksPageLocators.CART_LINK)
                )
                cart_link.click()
                logger.info("Clicked on the cart link. Navigating to the cart page.")

            # Agree to terms and proceed to checkout
            with allure.step("Agree to terms and proceed to checkout"):
                terms_checkbox = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(CheckoutPageLocators.TERMS_OF_SERVICE_CHECKBOX)
                )
                terms_checkbox.click()
                logger.info("Agreed to terms of service by clicking on the checkbox.")

                checkout_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable(CheckoutPageLocators.CHECKOUT_BUTTON)
                )
                checkout_button.click()
                logger.info("Clicked on the 'Proceed to Checkout' button.")

            # Verify the checkout form is displayed
            with allure.step("Verify checkout steps form is displayed"):
                WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located(CheckoutPageLocators.CHECKOUT_STEPS_FORM)
                )
                logger.info("Checkout form is displayed.")

        except Exception as e:
            logger.error(f"Test failed due to {str(e)}")
            allure.attach(driver.get_screenshot_as_png(), name="checkout_failure_screenshot",
                          attachment_type=allure.attachment_type.PNG)
            raise
