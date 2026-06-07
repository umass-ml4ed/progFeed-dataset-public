# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
import math

def is_leap_year(year):    
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
    

def list_leap_years(a, b):
    leap_years = []
    current_year = a
    while current_year <= b:
        if is_leap_year(current_year):
            leap_years.append(current_year)
        current_year += 1
    return leap_years