import allure
from hamcrest import assert_that, equal_to
from config.config import COMPUTERS_URL
from locators.computers_page_locators import ComputersPageLocators
from constants import EXPECTED_CATEGORY
from utils.browser_utils import BrowserUtils


class TestComputersCategory(BrowserUtils):

    @allure.feature('Computers Page')
    @allure.story('Verify Computers group has 3 sub-groups with correct names')
    def test_computers_sub_groups(self, driver):
        # Open the Computers category page using a utility function
        self.open_url(driver, COMPUTERS_URL)

        with allure.step('Retrieve and verify sub-categories'):
            # Retrieve all elements representing sub-categories
            category_items = self.wait_all_elements(driver, ComputersPageLocators.CATEGORY_ITEMS)
            # Extract the text (names) from the sub-category elements
            actual_category_names = [item.text for item in category_items]

            # Assert that the number of actual sub-categories matches the expected number
            assert_that(len(actual_category_names), equal_to(len(EXPECTED_CATEGORY)),
                        f"Expected number of sub-groups is 3, actual: {len(actual_category_names)}")

            # Assert that the actual names of the sub-categories match the expected names
            assert_that(actual_category_names, equal_to(EXPECTED_CATEGORY),
                        "Sub-groups have correct names")
