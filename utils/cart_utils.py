from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from hamcrest import assert_that, contains_string

from config.config import CART_URL, EMPTY_CART_MESSAGE_TEXT
from locators.cart_page_locators import CartPageLocators
from locators.books_page_locators import BooksPageLocators
from utils.notification_handler import NotificationHandler


class CartUtils:

    @staticmethod
    def clear_cart(driver):
        """Clear all items from the cart if there are any."""
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(CartPageLocators.CHECKBOXES)
        )
        checkboxes = driver.find_elements(*CartPageLocators.CHECKBOXES)
        if checkboxes:
            for checkbox in checkboxes:
                if not checkbox.is_selected():
                    checkbox.click()
            update_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(CartPageLocators.UPDATE_CART_BUTTON)
            )
            update_cart_button.click()
            WebDriverWait(driver, 20).until(
                EC.invisibility_of_element_located(CartPageLocators.CHECKBOXES)
            )
        empty_cart_message_element = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(CartPageLocators.EMPTY_CART_MESSAGE)
        )
        assert_that(empty_cart_message_element.text, contains_string(EMPTY_CART_MESSAGE_TEXT))
        driver.back()

    @staticmethod
    def get_cart_quantity(driver):
        """Get the quantity of items in the cart"""
        cart_quantity_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(BooksPageLocators.CART_QUANTITY)
        )
        return int(cart_quantity_element.text.strip('()'))

    @staticmethod
    def add_product_to_cart(driver, locator):
        """Add the first product on the books page to the cart"""
        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        add_to_cart_button.click()
        NotificationHandler.handle_notification(driver)

    @staticmethod
    def verify_notification(driver):
        """Verify that the notification appears and contains the correct text."""
        notification_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(BooksPageLocators.NOTIFICATION)
        )
        return notification_element.text

    @staticmethod
    def get_product_name(driver):
        """Get the name of the first product listed on the books page."""
        product_name_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(BooksPageLocators.ITEM_NAME)
        )
        return product_name_element.text
