# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_leap_year(year):
    if(year%400 == 0):
        return True
    elif(year%100 == 0 and year%400 != 0):
        return False
    elif(year%4 == 0 and year%100 != 0):
        return True
    else:
        return False
    
print(is_leap_year(2000))   # True (divisible by 400)
print(is_leap_year(1900))   # False (divisible by 100 but not 400)
print(is_leap_year(2012))   # True (divisible by 4 but not 100)
print(is_leap_year(2019)) 

def list_leap_years(a,b):
    result = []
    index = a
    while(index <= b):
        if(is_leap_year(index)):
            result.append(index)
        index +=1
    return result

print(list_leap_years(1995, 2005))
print(list_leap_years(1896, 1905))
print(list_leap_years(2019, 2021))
print(list_leap_years(2013, 2015))