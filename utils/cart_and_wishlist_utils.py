from locators.cart_page_locators import CartPageLocators
from utils.browser_utils import BrowserUtils
from utils.notification_handler import NotificationHandler


class CartAndWishlistUtils:
    @staticmethod
    def clear(driver, url):
        """Clear all items from the cart or wishlist if there are any."""
        BrowserUtils.open_url(driver, url)
        BrowserUtils.wait_for_element(driver, CartPageLocators.CHECKBOXES, 20)
        checkboxes = driver.find_elements(*CartPageLocators.CHECKBOXES)
        if checkboxes:
            for checkbox in checkboxes:
                if not checkbox.is_selected():
                    checkbox.click()
            BrowserUtils.wait_for_element_to_be_clickable(driver, CartPageLocators.UPDATE_CART_BUTTON, 20)
            BrowserUtils.wait_for_element_invisibility(driver, CartPageLocators.CHECKBOXES,20)

    @staticmethod
    def get_item_quantity(driver, locator, timeout=20):
        """Get the quantity of items in the Shopping Cart"""
        cart_quantity_element = BrowserUtils.wait_for_element(driver, locator, timeout)
        return int(cart_quantity_element.text.strip('()'))

    @staticmethod
    def add_product(driver, locator, timeout=30):
        """Add the product on the page to the cart or wishlist"""
        BrowserUtils.wait_for_element_to_be_clickable(driver, locator, timeout)
        NotificationHandler.handle_notification(driver)
