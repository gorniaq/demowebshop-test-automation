from selenium.webdriver.common.by import By

class LoginPageLocators:

    EMAIL_INPUT = (By.ID, "Email")
    PASSWORD_INPUT = (By.ID, "Password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input.login-button")
    ACCOUNT_LINK = (By.CSS_SELECTOR, "a.account")
