from selenium.webdriver.common.by import By


class WishlistLocators:

    APPAREL_SHOES_LINK = (By.LINK_TEXT, "Apparel & Shoes")
    PRODUCT_ITEM = (By.XPATH, "//div[@class='product-item' and @data-productid='5']")
    ADD_TO_WISHLIST_BUTTON = (By.ID, "add-to-wishlist-button-5")
