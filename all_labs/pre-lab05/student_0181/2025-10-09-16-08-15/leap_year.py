# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_leap_year(year):
    if year%4 == 0 and year %100 != 0: 
        return True 
    elif year %400 == 0:
        return True
    else:
        return False


def list_leap_years(a,b):
    lst = []
    while a <= b:
        if is_leap_year(a):
            lst.append(a)
        a+=1 
    return lst



