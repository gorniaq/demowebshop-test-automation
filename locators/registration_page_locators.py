from selenium.webdriver.common.by import By


class RegistrationPageLocators:

        GENDER_MALE = (By.ID, "gender-male")
        FIRST_NAME = (By.ID, "FirstName")
        LAST_NAME = (By.ID, "LastName")
        EMAIL = (By.ID, "Email")
        PASSWORD = (By.ID, "Password")
        CONFIRM_PASSWORD = (By.ID, "ConfirmPassword")
        REGISTER_BUTTON = (By.ID, "register-button")
        RESULT_MESSAGE = (By.CLASS_NAME, "result")
