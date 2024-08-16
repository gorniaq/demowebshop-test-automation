import pytest
import allure
from hamcrest import assert_that, equal_to
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import COMPUTERS_URL
from config.logger_config import logger
from drivers.driver_factory import DriverFactory
from locators.login_page_locators import LoginPageLocators
from config.config import LOGIN_URL, LOGIN_DATA
from utils.auth_utils import AuthUtils
from utils.browser_utils import BrowserUtils


class TestLogin:
    @allure.feature('Login Page')
    @allure.story('Verify that allows login a User')
    @pytest.mark.parametrize("browser_name", ["chrome", "firefox"])
    def test_login(self, browser_name):
        # Initialize the driver and open the login page
        driver = DriverFactory.get_driver(browser_name)
        # Use the utility to open the login URL
        BrowserUtils.open_url(driver, LOGIN_URL)

        try:
            with allure.step("Open the login page and perform login"):
                # Use the utility to open the login URL and log in
                AuthUtils.login(driver)

            with allure.step("Verify that the user is logged in and the correct account link is displayed"):
                account_link = WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located(LoginPageLocators.ACCOUNT_LINK)
                )
                assert_that(account_link.text, equal_to(LOGIN_DATA["email"]),
                            f"Expected account text to be '{LOGIN_DATA['email']}' but got '{account_link.text}'")

        except Exception as e:
            logger.error(f"Test failed due to {str(e)}")
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            raise

