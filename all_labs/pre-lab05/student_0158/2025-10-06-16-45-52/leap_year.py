# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_leap_year(year):
    if year%400==0:
        return True
    elif year%100==0 and year%400!=0:
        return False
    elif year%4==0 and year%100!=0:
        return True
    else:
        return False

def list_leap_years(a, b):
    leap_list=[]
    i=a
    while i<=b:
        if is_leap_year(i)==True:
            leap_list.append(i)
        i+=1
    return leap_list
