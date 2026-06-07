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
    while a <= b:
        is_leap_year(a)
        lst = []
        if is_leap_year(a) == True :
            return lst.append(a)
        else : 
            return []
        a = a+1

print(list_leap_years(1995, 2005))