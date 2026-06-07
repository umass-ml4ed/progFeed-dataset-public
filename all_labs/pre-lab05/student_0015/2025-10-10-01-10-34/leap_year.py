# Author: REDACTED
# Email: REDACTED
# SPIRE ID: REDACTED


''' A year is a leap year if:
It is divisible by 4
BUT if it's also divisible by 100, then it's not a leap year
UNLESS it’s divisible by 400! Then it is a leap year.
Your Task: Write a function to determine if a year is a leap year using nested branching!
'''
def is_leap_year(year):
    """
    Returns True if the given year is a leap year, otherwise False.
    """
    # A year is a leap year if divisible by 400,
    # or divisible by 4 but not by 100
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


def list_leap_years(a, b):
    """
    Returns a list of all leap years between a and b (inclusive).
    Must use a while loop.
    """
    leap_years = []
    year = a

    # Use while loop as required
    while year <= b:
        if is_leap_year(year):
            leap_years.append(year)
        year += 1

    return leap_years
