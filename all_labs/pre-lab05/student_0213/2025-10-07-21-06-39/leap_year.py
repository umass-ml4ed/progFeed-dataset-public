# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_leap_year(year):
    leap_year = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
    return leap_year

def list_leap_years(a, b):
    listy = []
    while a <= b:
        if is_leap_year(a) == True:
            listy.append(a)
        a += 1
    return listy