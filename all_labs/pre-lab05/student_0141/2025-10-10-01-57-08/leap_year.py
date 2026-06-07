# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_leap_year(year):
    """
    Returns True if 'year' is a leap year, else False.
    """
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

def list_leap_years(a, b):
    """
    Returns a list of all leap years from 'a' to 'b' (inclusive), using a while loop.
    """
    years = []
    current = a
    while current <= b:
        if is_leap_year(current):
            years.append(current)
        current += 1
    return years