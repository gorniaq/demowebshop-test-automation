import time
import pytest
import allure
from selenium import webdriver
from hamcrest import assert_that, contains_string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.logger_config import logger
from drivers.driver_factory import DriverFactory
from utils.auth_utils import AuthUtils
from locators.books_page_locators import BooksPageLocators
from config.config import BOOKS_URL, CART_URL, ADD_TO_CARt_SUCCESS_MESSAGE
# from utils.browser_utils import BrowserUtils


class TestAddToCart:
    # def test_cart_quantity(self, driver):
    #     cart_quantity_element = WebDriverWait(driver, 20).until(
    #         EC.visibility_of_element_located(BooksPageLocators.CART_QUANTITY)
    #     )
    #     return cart_quantity_element.text

    @allure.feature('Shopping Cart')
    @allure.story('Verify that a user can add an item to the cart')
    @pytest.mark.parametrize("browser_name", ["chrome", "firefox"])
    def test_add_to_cart(self, browser_name):
        driver = DriverFactory.get_driver(browser_name)
        AuthUtils.login(driver)

        try:
            with allure.step('d'):
                # BrowserUtils.clear_storage_and_cookies(driver)
                time.sleep(4)
            # with allure.step("Navigate to the products page"):
            #     driver.get(BOOKS_URL)
            #
            # with allure.step("Click on the 'Add to cart' button for the product"):
            #     add_to_cart_button = WebDriverWait(driver, 20).until(
            #         EC.element_to_be_clickable(BooksPageLocators.ADD_TO_CART)
            #     )
            #     add_to_cart_button.click()
            #
            # with allure.step("Verify that the notification appears and contains the correct text"):
            #     notification_element = WebDriverWait(driver, 20).until(
            #         EC.visibility_of_element_located(BooksPageLocators.NOTIFICATION)
            #     )
            #     notification_text = notification_element.text
            #     assert_that(notification_text, contains_string(ADD_TO_CARt_SUCCESS_MESSAGE))

            # with allure.step("Verify that the cart contains 1 item"):
            #     cart_quantity_text = self.test_cart_quantity(driver)
            #     assert_that(cart_quantity_text, contains_string("(1)"))
            # with allure.step("Click on the 'Shopping cart' link to navigate to the cart page"):
            #     cart_link = WebDriverWait(driver, 10).until(
            #         EC.element_to_be_clickable(BooksPageLocators.CART_LINK)
            #     )
            #     cart_link.click()
            #
            #     # Проверяем, что произошел переход на правильный URL
            #     WebDriverWait(driver, 10).until(
            #         EC.url_to_be(CART_URL)
            #     )
            #     assert driver.current_url == CART_URL, f"Expected URL to be {CART_URL}, but got {driver.current_url}"

            # Проверяем, что товар добавлен в корзину
            # with allure.step("Verify that the item was added to the cart"):
            #     cart_confirmation = WebDriverWait(driver, 20).until(
            #         EC.visibility_of_element_located(CartPageLocators.CART_CONFIRMATION_MESSAGE)
            #     )
            #     assert "The product has been added to your shopping cart" in cart_confirmation.text, (
            #         f"Expected confirmation message but got '{cart_confirmation.text}'"
            #     )

        except Exception as e:
            logger.error(f"Test failed due to {str(e)}")
            allure.attach(driver.get_screenshot_as_png(), name="add_to_cart_failure_screenshot",
                          attachment_type=allure.attachment_type.PNG)
            raise

