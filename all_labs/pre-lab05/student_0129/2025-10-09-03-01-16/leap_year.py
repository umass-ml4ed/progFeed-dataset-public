# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    if not year % 4 == 0:
        return False

def list_leap_years(a, b):
    year = a
    listy = []
    while year <= b:
        if is_leap_year(year):
            listy.append(year)
        year += 1
    return listy



