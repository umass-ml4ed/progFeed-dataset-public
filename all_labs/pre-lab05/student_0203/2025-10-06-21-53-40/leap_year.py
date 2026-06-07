# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_leap_year(year: int):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    elif year % 100 == 0 and year % 400 != 0:
        return False
    else:
        return False
    
def list_leap_years(a: int, b: int):
    leap_years = []
    while a <= b:
        if is_leap_year(a):
            leap_years.append(a)
        a += 1
    return leap_years