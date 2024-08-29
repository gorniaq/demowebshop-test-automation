from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    def submit_form(driver, locator):
        """
            Click a button to submit the form.
        """
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(locator)
        ).click()

    @staticmethod
    def logout(driver):
        """
           Logs out the user by clicking the logout link.
       """
        BrowserUtils.wait_for_element_to_be_clickable(driver, LoginPageLocators.LOGOUT_LINK, 20)

    @staticmethod
    def login(driver):
        """
            Log in as a user using predefined login data.
        """
        BrowserUtils.open_url(driver, LOGIN_URL)

        # Fill in the email and password fields using the utility method
        AuthUtils.fill_field(driver, LoginPageLocators.EMAIL_INPUT, LOGIN_DATA["email"])
        AuthUtils.fill_field(driver, LoginPageLocators.PASSWORD_INPUT, LOGIN_DATA["password"])

        # Submit the login form
        AuthUtils.submit_form(driver, LoginPageLocators.LOGIN_BUTTON)

        # Verify that the user is logged in
        account_link = BrowserUtils.wait_for_element(driver, LoginPageLocators.ACCOUNT_LINK, 20)
        logger.info(f"User logged in successfully, account link found: '{account_link.text}'")
