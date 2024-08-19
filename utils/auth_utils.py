import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import LOGIN_URL, LOGIN_DATA
from locators.login_page_locators import LoginPageLocators
from config.logger_config import logger
from utils.browser_utils import BrowserUtils


class AuthUtils:
    @staticmethod
    @allure.step("Log in as a user")
    def login(driver):
        try:
            with allure.step("Fill in the email and password"):
                # Wait for the email input field to be present and then input the email from LOGIN_DATA
                WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
                ).send_keys(LOGIN_DATA["email"])
                # Wait for the password input field to be present and then input the password from LOGIN_DATA
                WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located(LoginPageLocators.PASSWORD_INPUT)
                ).send_keys(LOGIN_DATA["password"])

            with allure.step("Submit the login form"):
                # Wait for the login button to be clickable and then click it to submit the form
                WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
                ).click()

            with allure.step("Verify that the user is logged in and the correct account link is displayed"):
                # Wait for the account link to be visible, then verify the text matches the expected email
                account_link = WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located(LoginPageLocators.ACCOUNT_LINK)
                )
                assert account_link.text == LOGIN_DATA["email"], (
                    f"Expected account text to be '{LOGIN_DATA['email']}' but got '{account_link.text}'"
                )

        except Exception as e:
            # If an exception occurs during the login process, log the error and attach a screenshot for debugging
            logger.error(f"Login failed due to {str(e)}")
            allure.attach(driver.get_screenshot_as_png(), name="login_failure_screenshot", attachment_type=allure.attachment_type.PNG)
            raise


