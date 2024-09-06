from dotenv import load_dotenv
import os

from locators.books_page_locators import BooksPageLocators

# Registration data for creating a new account
REGISTRATION_DATA = {
    "gender": "male",
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "password": "SecurePassword123",
    "confirm_password": "SecurePassword123"
}

# Success message displayed after successful registration
SUCCESS_MESSAGE = "Your registration completed"

# Expected categories on the products page
EXPECTED_CATEGORY = ["Desktops", "Notebooks", "Accessories"]

# Load environment variables from the .env file
load_dotenv()
# Use environment variables in your code
LOGIN_DATA = {
    "email": os.getenv('LOGIN_EMAIL'),
    "password": os.getenv('LOGIN_PASSWORD')
}

# Success message displayed when a product is added to the cart
ADD_TO_CART_SUCCESS_MESSAGE = "The product has been added to your shopping cart"

# Message displayed when the shopping cart is empty.
EMPTY_CART_MESSAGE_TEXT = 'Your Shopping Cart is empty!'

# Define sorting options and their expected behaviors
SORTING_OPTIONS = [
    BooksPageLocators.SORT_BY_POSITION,
    BooksPageLocators.SORT_BY_NAME_A_TO_Z,
    BooksPageLocators.SORT_BY_NAME_Z_TO_A,
    BooksPageLocators.SORT_BY_PRICE_LOW_TO_HIGH,
    BooksPageLocators.SORT_BY_PRICE_HIGH_TO_LOW,
    BooksPageLocators.SORT_BY_CREATED_ON
]

# List of page size options to be tested
OPTIONS_PAGE_SIZE = [
    BooksPageLocators.PAGE_SIZE_OPTION_4,
    BooksPageLocators.PAGE_SIZE_OPTION_8,
    BooksPageLocators.PAGE_SIZE_OPTION_12
]
