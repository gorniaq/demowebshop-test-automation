from hamcrest import assert_that, equal_to
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.logger_config import logger


class BrowserUtils:
    @staticmethod
    def open_url(driver, url, expected_url=None):
        """Opens a URL in the browser and optionally verifies that the correct URL is loaded.
        Args:
            driver (WebDriver): The WebDriver instance.
            url (str): The URL to open.
            expected_url (str, optional): The URL to verify after loading. Defaults to None.
        """
        driver.get(url)

        # If an expected URL is provided, verify it matches the current URL
        if expected_url:
            WebDriverWait(driver, 10).until(EC.url_to_be(expected_url))

    @staticmethod
    def check_url(driver: WebDriver, expected_url: str):
        """Checks if the current URL matches the expected URL.
                Args:
                    driver (WebDriver): The WebDriver instance.
                    expected_url (str): The expected URL to match.
        """
        WebDriverWait(driver, 10).until(
            EC.url_to_be(expected_url)
        )
        assert_that(driver.current_url, equal_to(expected_url))

    @staticmethod
    def scroll_to_element(driver, locator):
        """Scrolls the page until the specified element is in view.
        Args:
            driver (WebDriver): The WebDriver instance.
            locator (tuple): The locator of the element to scroll to, e.g., (By.ID, 'element_id').
        """
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        logger.info(f"Scrolled to element with locator: {locator}")

    @staticmethod
    def scroll_to_top(driver):
        """Scrolls to the top of the page.
        Args:
            driver (WebDriver): The WebDriver instance.
        """
        driver.execute_script("window.scrollTo(0, 0);")
        logger.info("Scrolled to the top of the page")