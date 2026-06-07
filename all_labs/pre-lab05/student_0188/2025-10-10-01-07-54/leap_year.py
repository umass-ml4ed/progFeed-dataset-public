# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_leap_year(year):
    # A leap year is divisible by 400, or divisible by 4 but not by 100
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

def list_leap_years(a, b):
    leap_years = []
    current_year = a

    while current_year <= b:
        if is_leap_year(current_year):
            leap_years.append(current_year)
        current_year += 1

    return leap_years

print(is_leap_year(2000))   # True
print(is_leap_year(1900))   # False
print(is_leap_year(2012))   # True
print(is_leap_year(2019))   # False

print(list_leap_years(1995, 2005))  # [1996, 2000, 2004]
print(list_leap_years(2013, 2015))  # []
