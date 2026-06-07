# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_leap_year(year):
    if year%400==0:
        return True
    elif year%4==0 and not year%100==0:
        return True
    else:
        return False
    
def list_leap_years(a,b):
    leap_years=[]
    while (a<=b):
        if is_leap_year(a):
            leap_years.append(a)
        a+=1
    return(leap_years)


