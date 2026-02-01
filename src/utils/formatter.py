# utils/formatter.py
# Contains utility functions for data formatting.

def format_currency(value, currency_symbol='$'):
    """
    Formats a numeric value into a currency string.

    Args:
        value (float or int): The numeric value to format.
        currency_symbol (str): The currency symbol to prepend.

    Returns:
        str: A string formatted as currency (e.g., "$123.45").
    """
    if not isinstance(value, (int, float)):
        return "N/A"
    return f"{currency_symbol}{value:.2f}"

