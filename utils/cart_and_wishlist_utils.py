from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from hamcrest import assert_that, contains_string

from config.config import CART_URL, EMPTY_CART_MESSAGE_TEXT
from locators.cart_page_locators import CartPageLocators
from locators.books_page_locators import BooksPageLocators
from utils.browser_utils import BrowserUtils
from utils.notification_handler import NotificationHandler


class CartAndWishlistUtils:
    @staticmethod
    def clear(driver, url):
        """Clear all items from the cart or wishlist if there are any."""
        BrowserUtils.open_url(driver, url)
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

    @staticmethod
    def get_items_quantity(driver, locator):
        """Get the quantity of items in the Shopping Cart"""
        cart_quantity_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        return int(cart_quantity_element.text.strip('()'))

    @staticmethod
    def add_product(driver, locator):
        """Add the product on the page to the cart or wishlist"""
        add_to_wishlist_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable(locator)
        )
        add_to_wishlist_button.click()
        NotificationHandler.handle_notification(driver)

    @staticmethod
    def get_product_name(driver, locator):
        """Get the name of the product listed on the books page."""
        product_name_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        return product_name_element.text

    @staticmethod
    def get_element_attribute(driver, locator, attribute):
        """
        Retrieves the value of a specified attribute from an element located by the provided locator.
        Args:
            driver (webdriver): The WebDriver instance used to interact with the browser.
            locator (tuple): A tuple containing the locator strategy and value to locate the element (e.g., (By.ID, 'element_id')).
            attribute (str): The name of the attribute whose value is to be retrieved.
        Returns:
            str: The value of the specified attribute from the located element.
        """
        # Wait until the element is visible on the page
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        # Retrieve the value of the specified attribute from the located element
        attribute_value = element.get_attribute(attribute)
        return attribute_value
