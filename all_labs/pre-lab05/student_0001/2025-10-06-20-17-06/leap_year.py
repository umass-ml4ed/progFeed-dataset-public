# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0 and year % 400 != 0:
        return False
    if year % 4 == 0 and year % 100 != 0:
        return True
    return False

# print(is_leap_year(2000))   
# print(is_leap_year(1900))   
# print(is_leap_year(2012))   
# print(is_leap_year(2019))

def list_leap_years(a,b):
    lst = []
    while a <= b:
        if is_leap_year(a):
            lst.append(a)
        a += 1
    return lst
        
# print(list_leap_years(1995, 2005))
# print(list_leap_years(1896, 1905))
# print(list_leap_years(2019, 2021))
# print(list_leap_years(2013, 2015))