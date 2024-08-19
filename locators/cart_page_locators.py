from selenium.webdriver.common.by import By


class CartPageLocators:

    CHECKBOXES = (By.CSS_SELECTOR, 'td.remove-from-cart input[name="removefromcart"]')
    UPDATE_CART_BUTTON = (By.CSS_SELECTOR, 'input[name="updatecart"]')
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, 'div.order-summary-content')

    ITEM_NAME = (By.CSS_SELECTOR, "td.product a.product-name")
    QUANTITY = (By.XPATH, "input.qty-input[name^='itemquantity']")
