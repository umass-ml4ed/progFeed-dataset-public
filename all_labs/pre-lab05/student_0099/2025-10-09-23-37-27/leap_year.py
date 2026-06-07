# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def is_leap_year(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)



print(is_leap_year(2000))
print(is_leap_year(1900)) 
print(is_leap_year(2012))  
print(is_leap_year(2019))  

def is_leap_year(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


def list_leap_years(a, b):
    leap_years = []
    year = a  
    
    while year <= b:  
        if is_leap_year(year):
            leap_years.append(year)
        year += 1  
    
    return leap_years



print(list_leap_years(1995, 2005))  
print(list_leap_years(1896, 1905)) 
print(list_leap_years(2019, 2021))  
print(list_leap_years(2013, 2015))  