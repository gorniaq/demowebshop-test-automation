from selenium.webdriver.common.by import By


class BooksPageLocators:

    SORT_BY_DROPDOWN = (By.ID, "products-orderby")

    SORT_BY_POSITION = (By.XPATH, "//option[@value='https://demowebshop.tricentis.com/books?orderby=0']")
    SORT_BY_NAME_A_TO_Z = (By.XPATH, "//option[@value='https://demowebshop.tricentis.com/books?orderby=5']")
    SORT_BY_NAME_Z_TO_A = (By.XPATH, "//option[@value='https://demowebshop.tricentis.com/books?orderby=6']")
    SORT_BY_PRICE_LOW_TO_HIGH = (By.XPATH, "//option[@value='https://demowebshop.tricentis.com/books?orderby=10']")
    SORT_BY_PRICE_HIGH_TO_LOW = (By.XPATH, "//option[@value='https://demowebshop.tricentis.com/books?orderby=11']")
    SORT_BY_CREATED_ON = (By.XPATH, "//option[@value='https://demowebshop.tricentis.com/books?orderby=15']")

    PRODUCT_TITLES = (By.CSS_SELECTOR, ".product-title a")
    PRODUCT_PRICES = (By.CSS_SELECTOR, ".prices .actual-price")

    PAGE_SIZE_DROPDOWN = (By.ID, 'products-pagesize')
    PAGE_SIZE_OPTION_4 = (By.XPATH, "//option[@value='https://demowebshop.tricentis.com/books?pagesize=4']")
    PAGE_SIZE_OPTION_8 = (By.XPATH, "//option[@value='https://demowebshop.tricentis.com/books?pagesize=8']")
    PAGE_SIZE_OPTION_12 = (By.XPATH, "//option[@value='https://demowebshop.tricentis.com/books?pagesize=12']")