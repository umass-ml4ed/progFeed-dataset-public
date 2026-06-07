# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_leap_year(year):
    if year % 400 == 0 or (year % 4 == 0 and not (year % 100 == 0)):
        return True
    else:
        return False

def list_leap_years(a, b):
    lis = []
    while a <= b:
        if is_leap_year(a):
            lis.append(a)
        else:
            a += 1
    return lis




