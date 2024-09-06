import allure
from hamcrest import assert_that, equal_to
from locators.registration_page_locators import RegistrationPageLocators
from config.config import REGISTER_URL
from constants import REGISTRATION_DATA, SUCCESS_MESSAGE
from config.logger_config import logger
from utils.auth_utils import AuthUtils
from utils.browser_utils import BrowserUtils
from utils.email_generator import EmailGenerator


class TestRegistrationPage(BrowserUtils, AuthUtils):

    @allure.feature('Registration')
    @allure.story('User can register with valid details')
    def test_registration(self, driver):

        # Use the utility to open the login URL
        self.open_url(driver, REGISTER_URL)

        # Initialize the WebDriver for the specified browser
        with allure.step('Filling out the registration form'):
            # Select gender radio button based on the gender specified in REGISTRATION_DATA
            gender_radio = self.wait_for_element(
                driver,
                RegistrationPageLocators.GENDER_MALE if REGISTRATION_DATA[
                                                            'gender'] == 'male' else RegistrationPageLocators.GENDER_FEMALE,
                20
            )
            gender_radio.click()
            logger.info(f'Selected gender: {REGISTRATION_DATA["gender"]}')

            # Generate a unique email for registration
            unique_email = EmailGenerator.generate_unique_email(REGISTRATION_DATA['email'])
            logger.info(f'Generated unique email: {unique_email}')

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
                self.fill_field(driver, locator, value)

        # Step to submit the registration form
        with allure.step('Submitting the registration form'):
            self.submit_form(driver, RegistrationPageLocators.REGISTER_BUTTON)

        # Step to verify that the registration was successful
        with (allure.step('Verifying successful registration')):
            # Verify that the success message is displayed and matches the expected message
            success_message = self.wait_for_element(driver, RegistrationPageLocators.RESULT_MESSAGE)
            assert_that(success_message.text, equal_to(SUCCESS_MESSAGE))
