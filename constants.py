from dotenv import load_dotenv
import os

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

EMPTY_CART_MESSAGE_TEXT = 'Your Shopping Cart is empty!'
