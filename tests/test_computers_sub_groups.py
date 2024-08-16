import pytest
import allure
from hamcrest import assert_that, equal_to
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import COMPUTERS_URL
from config.logger_config import logger
from drivers.driver_factory import DriverFactory
from locators.computers_page_locators import ComputersPageLocators
from config.config import EXPECTED_CATEGORY
from utils.browser_utils import BrowserUtils


class TestComputersCategory:
    @allure.feature('Computers Page')
    @allure.story('Verify Computers group has 3 sub-groups with correct names')
    @pytest.mark.parametrize("browser_name", ["chrome", "firefox"])
    def test_computers_sub_groups(self, browser_name):
        # Initialize the WebDriver for the specified browser
        driver = DriverFactory.get_driver(browser_name)
        # Open the Computers category page using a utility function
        BrowserUtils.open_url(driver, COMPUTERS_URL)

        try:
            with allure.step('Wait for the sub-category list to load'):
                # Log information about waiting for the sub-category list to load
                logger.info('Waiting for the sub-category list to load')
                # Wait until the sub-category list is present on the page
                WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located(ComputersPageLocators.CATEGORY_LIST)
                )

            with allure.step('Retrieve all sub-categories'):
                # Log information about retrieving the sub-categories
                logger.info('Retrieving all sub-categories')

                # Retrieve all elements representing sub-categories
                category_items = WebDriverWait(driver, 20).until(
                    EC.presence_of_all_elements_located(ComputersPageLocators.CATEGORY_ITEMS)
                )

                # Extract the text (names) from the sub-category elements
                actual_category_names = [item.text for item in category_items]

            with allure.step('Verify the number of sub-categories'):
                # Log information about verifying the number of sub-categories
                logger.info('Verifying the number of sub-categories')
                # Assert that the number of actual sub-categories matches the expected number
                assert_that(len(actual_category_names), equal_to(len(EXPECTED_CATEGORY)),
                            "Expected number of sub-groups is 3")

            with allure.step('Verify the names of the sub-categories'):
                # Log information about verifying the names of the sub-categories
                logger.info('Verifying the names of the sub-categories')
                # Assert that the actual names of the sub-categories match the expected names
                assert_that(actual_category_names, equal_to(EXPECTED_CATEGORY),
                            "Sub-groups have correct names")

        except Exception as e:
            # Log an error message if the test fails and attach a screenshot to the Allure report
            logger.error(f"Test failed due to {str(e)}")
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
            raise
