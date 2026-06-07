# Author : REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_leap_year(year):
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0

def list_leap_years(a,b):
    lis = []
    while a <= b:
        if is_leap_year(a):
            lis.append(a)
        a += 1
    return lis
