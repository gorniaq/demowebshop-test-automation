from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class DriverFactory:
    @staticmethod
    def get_driver(browser_name="chrome"):
        if browser_name == "chrome":
            options = webdriver.ChromeOptions()
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=options)
        elif browser_name == "firefox":
            options = webdriver.FirefoxOptions()
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=options)
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

        driver.implicitly_wait(10)  # Optional: set implicit wait time
        return driver
