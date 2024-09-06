import time


class EmailGenerator:
    @staticmethod
    def generate_unique_email(base_email):
        """
        Generates a unique email address by appending the current timestamp to the base email.
        """
        return f"{base_email.split('@')[0]}{int(time.time())}@{base_email.split('@')[1]}"
