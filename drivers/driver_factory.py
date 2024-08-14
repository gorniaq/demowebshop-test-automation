from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions


class DriverFactory:
    @staticmethod
    def get_driver(browser_name="chrome"):
        if browser_name == "chrome":
            chrome_options = ChromeOptions()
            chrome_options.add_argument("--headless")
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        elif browser_name == "firefox":
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.add_argument("--headless")
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

        return driver

    @staticmethod
    def close_driver(driver):
        if driver:
            if hasattr(driver, "service"):
                driver.service.stop()
            driver.quit()