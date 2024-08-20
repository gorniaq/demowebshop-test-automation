from dotenv import load_dotenv
import os

# URLs
BASE_URL = "https://demowebshop.tricentis.com/"
REGISTER_URL = "https://demowebshop.tricentis.com/register"
COMPUTERS_URL = "https://demowebshop.tricentis.com/computers"
LOGIN_URL = "https://demowebshop.tricentis.com/login"
BOOKS_URL = "https://demowebshop.tricentis.com/books"
CART_URL = "https://demowebshop.tricentis.com/cart"
WISHLIST_URL = "https://demowebshop.tricentis.com/wishlist"

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
