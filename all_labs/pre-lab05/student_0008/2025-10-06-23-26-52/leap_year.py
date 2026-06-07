# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False
    
def list_leap_years(a, b):
    leapList = []
    year = a
    while year <= b:
        if is_leap_year(year) == True:
            leapList.append(year)
        year = year + 1
    return leapList