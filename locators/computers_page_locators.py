from selenium.webdriver.common.by import By


class ComputersPageLocators:

    CATEGORY_LIST = (By.CLASS_NAME, "sub-category-grid")
    CATEGORY_ITEMS = (By.CSS_SELECTOR, ".sub-category-item .title a")
