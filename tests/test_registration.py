import time
import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from hamcrest import assert_that, equal_to
from drivers.driver_factory import DriverFactory
from locators.loginPageLocators import LoginPageLocators
from config.config import REGISTER_URL, REGISTRATION_DATA, SUCCESS_MESSAGE
from config.logger_config import logger


@allure.feature('Registration')
@allure.story('User can register with valid details')
@pytest.mark.parametrize("browser_name", ["chrome", "firefox"])
def test_registration(browser_name):
    driver = DriverFactory.get_driver(browser_name)
    driver.get(REGISTER_URL)

    try:
        with allure.step('Filling out the registration form'):
            logger.info('Filling out the registration form')
            gender_radio = WebDriverWait(driver, 20).until(EC.presence_of_element_located(LoginPageLocators.GENDER_MALE if REGISTRATION_DATA['gender'] == 'male' else LoginPageLocators.GENDER_FEMALE))
            gender_radio.click()

            unique_email = f"{REGISTRATION_DATA['email'].split('@')[0]}{int(time.time())}@{REGISTRATION_DATA['email'].split('@')[1]}"
            fields = {
                LoginPageLocators.FIRST_NAME: REGISTRATION_DATA['first_name'],
                LoginPageLocators.LAST_NAME: REGISTRATION_DATA['last_name'],
                LoginPageLocators.EMAIL: unique_email,
                LoginPageLocators.PASSWORD: REGISTRATION_DATA['password'],
                LoginPageLocators.CONFIRM_PASSWORD: REGISTRATION_DATA['confirm_password'],
            }

            for locator, value in fields.items():
                WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located(locator)
                ).send_keys(value)

        with allure.step('Submitting the registration form'):
            logger.info('Submitting the registration form')
            register_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(LoginPageLocators.REGISTER_BUTTON)
            )
            register_button.click()

        with allure.step('Verifying successful registration'):
            logger.info('Verifying successful registration')

            success_message = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located(LoginPageLocators.RESULT_MESSAGE)
            )
            assert_that(success_message.text, equal_to(SUCCESS_MESSAGE))

    except Exception as e:
        logger.error(f"Test failed due to {str(e)}")
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
        raise

    finally:
        driver.quit()

