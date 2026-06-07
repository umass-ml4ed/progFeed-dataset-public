# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_leap_year(year):
    return (year % 400 == 0) or (year % 100 == 0 and year % 400 == 0) or (year % 4 == 0 and year % 100 != 00)

def list_leap_years(a,b):
    leap_year = []
    while a <= b:
        if is_leap_year(a):
            leap_year.append(a)
        a = a + 1
    return leap_year


#print(list_leap_years(1995, 2005))   
#print(list_leap_years(1896, 1905))
#print(list_leap_years(2019, 2021))
#print(list_leap_years(2013, 2015))

#print(is_leap_year(2000))   # True (divisible by 400)
#print(is_leap_year(1900))   # False (divisible by 100 but not 400)
#print(is_leap_year(2012))   # True (divisible by 4 but not 100)
#print(is_leap_year(2019))   # False (not divisible by 4)