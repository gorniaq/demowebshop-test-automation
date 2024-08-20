from selenium.webdriver.common.by import By


class CartPageLocators:

    CART_QUANTITY = (By.XPATH, "//a[@class='ico-cart']//span[@class='cart-qty']")

    CHECKBOXES = (By.CSS_SELECTOR, 'td.remove-from-cart input[name="removefromcart"]')
    UPDATE_CART_BUTTON = (By.CSS_SELECTOR, 'input[name="updatecart"]')
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, 'div.order-summary-content')

    ITEM_NAME = (By.CSS_SELECTOR, "td.product a.product-name")
    QUANTITY_IN_CART = (By.CSS_SELECTOR, "input.qty-input")
