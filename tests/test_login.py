import pytest
import allure
from hamcrest import assert_that, equal_to
from locators.login_page_locators import LoginPageLocators
from config.config import LOGIN_URL
from constants import LOGIN_DATA
from utils.auth_utils import AuthUtils
from utils.browser_utils import BrowserUtils


class TestLogin(BrowserUtils, AuthUtils):
    @allure.feature('Login Page')
    @allure.story('Verify that allows login a User')
    @pytest.mark.parametrize("driver", ["chrome", "firefox"], indirect=True)
    def test_login(self, driver):
        # Use the utility to open the login URL
        with allure.step("Open URL"):
            self.open_url(driver, LOGIN_URL)

        with allure.step("Fill in the email and password"):
            # Wait for the email input field to be present and then input the email from LOGIN_DATA
            self.fill_field(driver, LoginPageLocators.EMAIL_INPUT, LOGIN_DATA["email"])
            # Wait for the password input field to be present and then input the password from LOGIN_DATA
            self.fill_field(driver, LoginPageLocators.PASSWORD_INPUT, LOGIN_DATA["password"])

        with allure.step("Submit the login form"):
            # Wait for the login button to be clickable and then click it to submit the form
            self.submit_form(driver, LoginPageLocators.LOGIN_BUTTON)

        with allure.step("Verify that the user is logged in and the correct account link is displayed"):
            account_link = self.wait_for_element(driver, LoginPageLocators.ACCOUNT_LINK, 20)

            # Verify that the account link text matches the expected email
            assert_that(account_link.text, equal_to(LOGIN_DATA["email"]),
                        f"Expected account text to be '{LOGIN_DATA['email']}' but got '{account_link.text}'")

        with allure.step("Click on 'Log out' to log out of the account"):
            self.logout(driver)
