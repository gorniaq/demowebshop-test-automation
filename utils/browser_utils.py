from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.logger_config import logger


class BrowserUtils:
    @staticmethod
    def open_url(driver, url, expected_url=None):
        """Opens a URL in the browser and optionally verifies that the correct URL is loaded.
        """
        driver.get(url)

        # If an expected URL is provided, verify it matches the current URL
        if expected_url:
            WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))

    @staticmethod
    def wait_for_element(driver, locator, timeout=20):
        """Waits for an element to be present in the DOM and returns it.
        Returns:
            WebElement: The located element.
        """
        return WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @staticmethod
    def wait_for_element_and_click(driver, locator, timeout=20):
        """
        Wait for an element to be clickable.
        """
        return WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(locator)
        ).click()

    @staticmethod
    def wait_for_element_invisibility(driver, locator, timeout=20):
        """
        Waits until the element specified by the locator becomes invisible on the page.
        """
        return WebDriverWait(driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @staticmethod
    def wait_all_elements(driver, locator, timeout=20):
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    @staticmethod
    def scroll_to_element(driver, locator):
        """Scrolls the page until the specified element is in view.
        """
        element = BrowserUtils.wait_for_element(driver, locator, 20)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        logger.info(f"Scrolled to element with locator: {locator}")

    @staticmethod
    def scroll_to_top(driver):
        """Scrolls to the top of the page.
        """
        driver.execute_script("window.scrollTo(0, 0);")
        logger.info("Scrolled to the top of the page")

    @staticmethod
    def get_elements(driver, locator):
        """
        Retrieve all elements located by the given locator.
        """
        BrowserUtils.wait_all_elements(driver, locator)
        return driver.find_elements(*locator)

    @staticmethod
    def get_actual_products_count(driver, locator):
        """Retrieve the count of items matching the locator."""
        return len(BrowserUtils.get_elements(driver, locator))

    @staticmethod
    def select_dropdown_option_by_text(driver, locator):
        """
        Select an option from a dropdown by clicking on the item and return the text of the selected option.
        Returns:
            str: The text of the selected dropdown option.
        """
        option = BrowserUtils.wait_for_element(driver, locator, 20)
        option_text = option.text.strip()
        option.click()
        return option_text

    @staticmethod
    def select_dropdown_option_by_number(driver, locator):
        """
        Select an option from a dropdown by clicking on the item and return the number of items.
        Returns:
            int: The number of items per page.
        """
        option_text = BrowserUtils.select_dropdown_option_by_text(driver, locator)
        return int(option_text)  # Convert the text to an integer

    @staticmethod
    def get_product_title(driver, locator, timeout=20):
        """Get the name of the product listed on the books page."""
        product_name_element = BrowserUtils.wait_for_element(driver, locator, timeout)
        return product_name_element.text

    @staticmethod
    def get_element_attribute(driver, locator, attribute):
        """
        Retrieves the value of a specified attribute from an element located by the provided locator.
        """
        # Wait until the element is visible on the page
        element = BrowserUtils.wait_for_element(driver, locator, 10)
        # Retrieve the value of the specified attribute from the located element
        attribute_value = element.get_attribute(attribute)
        return attribute_value
