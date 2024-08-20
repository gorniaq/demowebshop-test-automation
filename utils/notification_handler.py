from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.logger_config import logger
from locators.books_page_locators import BooksPageLocators


class NotificationHandler:

    @staticmethod
    def wait_for_notification_to_disappear(driver, timeout=20):
        """
        Wait for the notification to disappear from the page.
        Args:
            driver: The WebDriver instance used to interact with the browser.
            timeout: Maximum time (in seconds) to wait for the notification to disappear.
        """
        try:
            # Wait until the notification is no longer visible on the page
            WebDriverWait(driver, timeout).until(
                EC.invisibility_of_element_located(BooksPageLocators.NOTIFICATION)
            )
            logger.info("Notification has disappeared.")
        except TimeoutException:
            # Log a warning if the notification did not disappear within the given timeout
            logger.warning("Notification did not disappear within the given timeout.")

    @staticmethod
    def close_notification(driver):
        """
        Close the notification if it is present.
        Args:
            driver: The WebDriver instance used to interact with the browser.
        """
        try:
            # Wait until the notification close button is clickable
            close_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(BooksPageLocators.NOTIFICATION_CLOSE_BTN)
            )
            close_button.click()  # Click the close button to close the notification
            logger.info("Notification was closed.")
        except TimeoutException:
            # Log info if the notification close button was not present or clickable
            logger.info("Notification close button was not present or clickable.")

    @staticmethod
    def handle_notification(driver):
        """
        Handle the notification: close it if present, or wait for it to disappear.
        Args:
            driver: The WebDriver instance used to interact with the browser.
        """
        # Attempt to close the notification
        NotificationHandler.close_notification(driver)
        # Wait for the notification to disappear if it was not closed
        NotificationHandler.wait_for_notification_to_disappear(driver)

    # @staticmethod
    # def get_notification_text(driver):
    #     """
    #     Get the text from the notification if it is present.
    #     Args:
    #         driver: The WebDriver instance used to interact with the browser.
    #     Returns:
    #         The text of the notification if present; otherwise, an empty string.
    #     """
    #     try:
    #         # Wait until the notification is visible
    #         notification_element = WebDriverWait(driver, 10).until(
    #             EC.visibility_of_element_located(BooksPageLocators.NOTIFICATION)
    #         )
    #         # Get the text of the notification
    #         notification_text = notification_element.text
    #         logger.info(f"Notification text: {notification_text}")
    #         return notification_text
    #     except TimeoutException:
    #         logger.info("No notification found.")
    #         return ""
