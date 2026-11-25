
from datetime import datetime

VALID_CATEGORIES = {
    "Food",
    "Transport",
    "Utilities",
    "Entertainment",
    "Other"
}


def validate_amount(value):
    """Check that the amount is a positive number."""
    if isinstance(value, bool):
        return False

    try:
        amount = float(value)
        return amount > 0
    except (ValueError, TypeError):
        return False


def validate_date(date_string):
    """Check date format YYYY-MM-DD."""
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return (
            len(date_string) == 10
            and date_string[4] == "-"
            and date_string[7] == "-"
            and date_string == datetime.strptime(
                date_string, "%Y-%m-%d"
            ).strftime("%Y-%m-%d")
        )
    except (ValueError, TypeError):
        return False


def validate_category(category):
    """Check whether the category is valid."""
    if not isinstance(category, str):
        return False

    return category.strip().title() in VALID_CATEGORIES
