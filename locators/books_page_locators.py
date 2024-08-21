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

    ADD_TO_CART = (By.XPATH, "//input[@class='button-2 product-box-add-to-cart-button' and @value='Add to cart']")
    ITEM_PRODUCT = (By.XPATH, "//div[@class='product-item']//a[@href='/computing-and-internet']")
    ITEM_NAME = (By.XPATH, "//h2[@class='product-title']/a")
    ITEM_LINK = (By.XPATH, "//a[contains(@href, '/computing-and-internet')]")
    CART_QUANTITY = (By.XPATH, "//a[@class='ico-cart']//span[@class='cart-qty']")
    CART_LINK = (By.XPATH, "//*[@id ='topcartlink']/a")
    NOTIFICATION = (By.CSS_SELECTOR, "div.bar-notification.success")
    NOTIFICATION_CLOSE_BTN = (By.CSS_SELECTOR, "#bar-notification .close")

    # Locator for the 'Add to cart' button of the first item on the page
    FIRST_ITEM_ADD_TO_CART = (By.XPATH, '//input[@id="add-to-cart-button-13"]')



