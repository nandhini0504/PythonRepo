import re

def validate_email(email):
    # Regular expression pattern for validating email addresses
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    # Use the re.match function to check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False