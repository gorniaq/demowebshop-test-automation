class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def navigate_to(self, by_locator):
        self.driver.find_element(*by_locator).click()
