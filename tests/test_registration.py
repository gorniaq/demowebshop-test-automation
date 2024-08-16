import time
import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from hamcrest import assert_that, equal_to
from drivers.driver_factory import DriverFactory
from locators.registration_page_locators import RegistrationPageLocators
from config.config import REGISTER_URL, REGISTRATION_DATA, SUCCESS_MESSAGE
from config.logger_config import logger
from utils.browser_utils import BrowserUtils


class TestRegistrationPage:
    @staticmethod
    def generate_unique_email(base_email):
        """Generates a unique email address by appending the current timestamp to the base email.
        Args:
            base_email (str): The base email address to be modified.
        Returns:
            str: A unique email address.
        """
        return f"{base_email.split('@')[0]}{int(time.time())}@{base_email.split('@')[1]}"

    @allure.feature('Registration')
    @allure.story('User can register with valid details')
    @pytest.mark.parametrize("browser_name", ["chrome", "firefox"])
    def test_registration(self, browser_name):
        driver = DriverFactory.get_driver(browser_name)
        BrowserUtils.open_url(driver, REGISTER_URL)

        try:
            # Initialize the WebDriver for the specified browser
            with allure.step('Filling out the registration form'):
                logger.info('Filling out the registration form')
                # Select gender radio button based on the gender specified in REGISTRATION_DATA
                gender_radio = WebDriverWait(driver, 20).until(EC.presence_of_element_located(RegistrationPageLocators.GENDER_MALE if REGISTRATION_DATA['gender'] == 'male' else RegistrationPageLocators.GENDER_FEMALE))
                gender_radio.click()

                # Generate a unique email for registration
                unique_email = self.generate_unique_email(REGISTRATION_DATA['email'])

                # Prepare a dictionary of form fields and their corresponding values
                fields = {
                    RegistrationPageLocators.FIRST_NAME: REGISTRATION_DATA['first_name'],
                    RegistrationPageLocators.LAST_NAME: REGISTRATION_DATA['last_name'],
                    RegistrationPageLocators.EMAIL: unique_email,
                    RegistrationPageLocators.PASSWORD: REGISTRATION_DATA['password'],
                    RegistrationPageLocators.CONFIRM_PASSWORD: REGISTRATION_DATA['confirm_password'],
                }

                # Fill in each field with the provided data
                for locator, value in fields.items():
                    WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located(locator)
                    ).send_keys(value)

            # Step to submit the registration form
            with allure.step('Submitting the registration form'):
                logger.info('Submitting the registration form')
                register_button = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located(RegistrationPageLocators.REGISTER_BUTTON)
                )
                # Locate and click the 'Register' button
                register_button.click()

            # Step to verify that the registration was successful
            with allure.step('Verifying successful registration'):
                logger.info('Verifying successful registration')

                # Verify that the success message is displayed and matches the expected message
                success_message = WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located(RegistrationPageLocators.RESULT_MESSAGE)
                )
                assert_that(success_message.text, equal_to(SUCCESS_MESSAGE))

        except Exception as e:
            # Log the error and attach a screenshot to the Allure report if the test fails
            logger.error(f"Test failed due to {str(e)}")
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            # Re-raise the exception to fail the test
            raise



