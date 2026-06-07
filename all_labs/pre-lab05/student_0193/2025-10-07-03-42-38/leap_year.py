# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_leap_year (year: int):
    if year % 100 == 0 and not year % 400 == 0:
        return False
    if year % 400 == 0:
        return True
    if year % 4 == 0 and not year % 100 == 0:
        return True
    else:
        return False