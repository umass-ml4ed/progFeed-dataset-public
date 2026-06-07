# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_leap_year(y):
    if y % 400 == 0:
        return True
    elif y % 100 == 0:
        return False
    elif y % 4 == 0:
        return True
    else:
        return False

def list_leap_years(y1: int,y2: int):
    years = []
    while y2 >= y1:
        if is_leap_year(y1):
            years.append(y1)
        y1 += 1
    return years
