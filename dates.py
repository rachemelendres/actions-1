from datetime import datetime


def get_date_string(date: datetime) -> str:
    """Get a date string in the format YYYY-MM-DD."""
    return date.strftime('%Y-%m-%d')
