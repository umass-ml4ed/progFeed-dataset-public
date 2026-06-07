# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_leap_year(year):
    if year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
    
def list_leap_years(a, b):
    year_list = []
    for year in range(a,b+1):
        if is_leap_year(year) == True:
            year_list.append(year)
    return year_list