# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_leap_year(year):
    if year % 400 ==0:
        return True
    elif year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else: 
        return False

def list_leap_years(a,b):
    while a <=b:
        if is_leap_year(a):
            print(a)
        a += 1 

    return