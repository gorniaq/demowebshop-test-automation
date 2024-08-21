import pytest
import allure
from hamcrest import assert_that, equal_to
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.logger_config import logger
from locators.login_page_locators import LoginPageLocators
from config.config import LOGIN_URL, LOGIN_DATA
from utils.auth_utils import AuthUtils
from utils.browser_utils import BrowserUtils


class TestLogin(AuthUtils):
    @allure.feature('Login Page')
    @allure.story('Verify that allows login a User')
    @pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
    # The "indirect=True" flag ensures that the values ("chrome" and "firefox")
    def test_login(self, driver):
        # Initialize the WebDriver for the specified browser
        logger.info(f"Initialized WebDriver for {driver}")

        # Use the utility to open the login URL
        BrowserUtils.open_url(driver, LOGIN_URL)
        logger.info(f"Opened login URL: {LOGIN_URL}")

        try:
            with allure.step("Fill in the email and password"):
                # Wait for the email input field to be present and then input the email from LOGIN_DATA
                self.fill_field(driver, LoginPageLocators.EMAIL_INPUT, LOGIN_DATA["email"])
                # Wait for the password input field to be present and then input the password from LOGIN_DATA
                self.fill_field(driver, LoginPageLocators.PASSWORD_INPUT, LOGIN_DATA["password"])

            with allure.step("Submit the login form"):
                # Wait for the login button to be clickable and then click it to submit the form
                self.submit_form(driver, LoginPageLocators.LOGIN_BUTTON)

            with allure.step("Verify that the user is logged in and the correct account link is displayed"):
                account_link = WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located(LoginPageLocators.ACCOUNT_LINK)
                )
                logger.info(f"Account link text found: '{account_link.text}'")

                # Verify that the account link text matches the expected email
                assert_that(account_link.text, equal_to(LOGIN_DATA["email"]),
                            f"Expected account text to be '{LOGIN_DATA['email']}' but got '{account_link.text}'")
                logger.info("Login verification passed. Account link text is as expected.")

                with allure.step("Click on 'Log out' to log out of the account"):
                    self.logout(driver)
                    logger.info("Clicked on 'Log out' successfully.")

        except Exception as e:
            # Log the error and attach a screenshot to the Allure report
            logger.error(f"Test failed due to {str(e)}")
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            raise
