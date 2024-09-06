import allure
from config.config import LOGIN_URL
from constants import LOGIN_DATA
from locators.login_page_locators import LoginPageLocators
from config.logger_config import logger
from utils.browser_utils import BrowserUtils


class AuthUtils:

    @staticmethod
    def fill_field(driver, locator, value):
        """
        Fill in a web form field with the provided data.
        """
        BrowserUtils.wait_for_element(driver, locator, 20).send_keys(value)
        logger.info(f"Field located by {locator} filled with data: '{value}'")

    @staticmethod
    def submit_form(driver, locator,  timeout=20):
        """
        Click a button to submit the form.
        """
        BrowserUtils.wait_for_element_and_click(driver, locator, timeout)

    @staticmethod
    def logout(driver, timeout=20):
        """
        Logs out the user by clicking the logout link.
        """
        BrowserUtils.wait_for_element_and_click(driver, LoginPageLocators.LOGOUT_LINK, timeout)

    @staticmethod
    def login(driver, timeout=20):
        """
        Log in as a user using predefined login data.
        """
        with allure.step("Log in to the application"):
            BrowserUtils.open_url(driver, LOGIN_URL)

            # Fill in the email and password fields using the utility method
            AuthUtils.fill_field(driver, LoginPageLocators.EMAIL_INPUT, LOGIN_DATA["email"])
            AuthUtils.fill_field(driver, LoginPageLocators.PASSWORD_INPUT, LOGIN_DATA["password"])

            # Submit the login form
            AuthUtils.submit_form(driver, LoginPageLocators.LOGIN_BUTTON)

            # Verify that the user is logged in
            account_link = BrowserUtils.wait_for_element(driver, LoginPageLocators.ACCOUNT_LINK, timeout)
            logger.info(f"User logged in successfully, account link found: '{account_link.text}'")
