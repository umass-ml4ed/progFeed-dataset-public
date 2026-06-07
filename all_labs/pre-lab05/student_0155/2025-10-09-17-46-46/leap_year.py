# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_leap_year(year):
    return (year % 400 == 0) or ((year % 4 == 0) and year % 100 != 0)

#print(is_leap_year(2000))
#print(is_leap_year(1900))
#print(is_leap_year(2012))
#print(is_leap_year(2019))

def list_leap_years(a,b):
    n = 0
    newlst = []
    year_range = range(a,b+1)
    while n < len(year_range):
        if is_leap_year(year_range[n]):
            newlst.append(year_range[n])
        n += 1
    return newlst

#print(list_leap_years(1995, 2004))    
#print(list_leap_years(1896, 1905))