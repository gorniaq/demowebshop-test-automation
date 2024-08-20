from selenium.webdriver.common.by import By


class WishlistPageLocators:

    WISHLIST_QTY = (By.CSS_SELECTOR, "a.ico-wishlist .wishlist-qty")
    WISHLIST_LINK = (By.CSS_SELECTOR, "a.ico-wishlist")

    APPAREL_SHOES_LINK = (By.XPATH, "//ul[@class='top-menu']//a[@href='/apparel-shoes']")

    PRODUCT_ITEM = (By.XPATH, "//a[@href='/50s-rockabilly-polka-dot-top-jr-plus-size']")

    WISHLIST_ITEM_NAME = (By.XPATH, "//div[@class='product-item' and @data-productid='5']//h2[@class='product-title']/a")
    ADD_TO_WISHLIST_BUTTON = (By.ID, "add-to-wishlist-button-5")

    QUANTITY_WISLIST_PAGE = (By.XPATH, "//td[@class='qty nobr']//input[@class='qty-input valid']")



