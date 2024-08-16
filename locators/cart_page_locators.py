from selenium.webdriver.common.by import By


class CartPageLocators:

    ITEM_NAME = (By.CSS_SELECTOR, "td.product a.product-name")
    QUANTITY = (By.XPATH, "input.qty-input[name^='itemquantity']")
