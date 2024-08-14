import pytest
from drivers.driver_factory import DriverFactory

@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("--browser")
    driver = DriverFactory.get_driver(browser_name)
    yield driver
    DriverFactory.close_driver(driver)
