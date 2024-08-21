import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import LOGIN_URL, LOGIN_DATA
from locators.login_page_locators import LoginPageLocators
from config.logger_config import logger
from utils.browser_utils import BrowserUtils


class AuthUtils:

    @staticmethod
    def fill_field(driver, locator, value):
        """
        Fill in a web form field with the provided data.
        Args:
            driver (WebDriver): The WebDriver instance to use for interacting with the browser.
            locator (tuple): Locator for the web form field (e.g., (By.ID, 'field_id')).
            value (str): The data to input into the form field.
        """
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(locator)
        ).send_keys(value)
        logger.info(f"Field located by {locator} filled with data: '{value}'")

    @staticmethod
    def submit_form(driver, locator):
        """
            Click a button to submit the form.
            Args:
                driver (WebDriver): The WebDriver instance to use for interacting with the browser.
                locator (tuple): Locator for the submit button (e.g., (By.ID, 'submit_button')).
        """
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(locator)
        ).click()

    @staticmethod
    def logout(driver):
        logout_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGOUT_LINK)
        )
        logout_link.click()

    @staticmethod
    def login(driver):
        """
                Log in as a user using predefined login data.
                Args:
                    driver (WebDriver): The WebDriver instance to use for interacting with the browser.
                """
        BrowserUtils.open_url(driver, LOGIN_URL)

        # Fill in the email and password fields using the utility method
        AuthUtils.fill_field(driver, LoginPageLocators.EMAIL_INPUT, LOGIN_DATA["email"])
        AuthUtils.fill_field(driver, LoginPageLocators.PASSWORD_INPUT, LOGIN_DATA["password"])

        # Submit the login form
        AuthUtils.submit_form(driver, LoginPageLocators.LOGIN_BUTTON)

        # Verify that the user is logged in
        account_link = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(LoginPageLocators.ACCOUNT_LINK)
        )
        logger.info(f"User logged in successfully, account link found: '{account_link.text}'")
