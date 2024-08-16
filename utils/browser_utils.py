from hamcrest import assert_that, equal_to
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        WebDriverWait(driver, 10).until(
            EC.url_to_be(expected_url)
        )
        assert_that(driver.current_url, equal_to(expected_url))
