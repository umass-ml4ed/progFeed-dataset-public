# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_leap_year(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        return True
    else:
        return False
    
print(is_leap_year(2000))  
print(is_leap_year(1900))   
print(is_leap_year(2012))   
print(is_leap_year(2019)) 

def list_leap_years(a,b):
    if a>b:
        raise ValueError("Expected a<=b")

    result=[]
    year=a
    while year<=b:
        if is_leap_year(year):
            result.append(year)
        year=year+1
    return result

print(list_leap_years(1995, 2005))
print(list_leap_years(1896, 1905))
print(list_leap_years(2019, 2021))
print(list_leap_years(2013, 2015))
