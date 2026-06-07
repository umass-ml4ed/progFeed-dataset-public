# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

'''A leap year is defined as:
Years divisible by 400 are leap years.
Years divisible by 100 but not 400 are not leap years.
Years divisible by 4 but not 100 are leap years.
All other years are not leap years.
Write a function, called is_leap_year, inside  leap_year.py, which should:
Take a single integer parameter year
Return boolean True if the year is a leap year, otherwise return boolean False
'''

def is_leap_year(year) -> bool:
    if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
        return True
    else:
        return False
       
print(is_leap_year(2000))   # True (divisible by 400)
print(is_leap_year(1900))   # False (divisible by 100 but not 400)
print(is_leap_year(2012))   # True (divisible by 4 but not 100)
print(is_leap_year(2019))   # False (not divisible by 4)

'''Take two integer parameters a and b (with a <= b)
Use a while loop to check every year between a and b (inclusive)
Return a list of all years that are leap years in that range
Important notes:
You must use a while loop in your implementation.
You may call your is_leap_year function from the previous problem to check each year.
Return a list of integers, not strings.
If no leap years are found, return an empty list [].'''


def list_leap_years(y1, y2):
    lis = []
    y = y1
    while y <= y2:
        if is_leap_year(y) == True:
            lis.append(y)
        y += 1
    return lis
        
print(list_leap_years(1990, 2025))
# Output: [1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024]

'''def list_leap_years(y1, y2):
    result = []
    year = a
    while year <= b:
        if is_leap_year(year):
            result.append(year)
        year += 1
    return result'''