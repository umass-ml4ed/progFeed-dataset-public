# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_leap_year(year):
    return (year % 400 == 0) or ((year % 100 != 0) and (year % 4 == 0))

def list_leap_years(a, b):
    list_of_leap = []
    while (a <= b):
        if is_leap_year(a):
            list_of_leap.append(a)
        a += 1
    return list_of_leap