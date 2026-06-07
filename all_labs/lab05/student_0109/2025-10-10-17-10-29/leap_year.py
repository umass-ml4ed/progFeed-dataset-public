#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

def is_leap_year(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        return True
    else:
        return False

def list_leap_years(a,b):
    i=a
    lst = []
    while i<=b:
        if is_leap_year(i):
            lst.append(i)
        i += 1
    return lst
