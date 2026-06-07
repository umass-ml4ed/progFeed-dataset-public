# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED



def is_leap_year(year):
    if year%400 == 0:
        return True
    elif year%100 == 0 and not year%400 == 0:
        return False
    elif year%4 == 0 and not year%100 == 0:
        return True
    else:
        return False
    

def list_leap_years(a,b):
    lst = []
    yr = a 
    while yr<=b:
        if is_leap_year(yr):
            lst.append(int(yr))
        yr +=1
    return lst




