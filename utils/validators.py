from email_validator import validate_email
from email_validator import EmailNotValidError

def validate_user_data(data):

    required_fields = [
        "name",
        "email",
        "role"
    ]

    for field in required_fields:

        if field not in data or not data[field]:

            return False, f"{field} is required"

    try:

        validate_email(data["email"])

    except EmailNotValidError:

        return False, "Invalid email format"

    return True, None