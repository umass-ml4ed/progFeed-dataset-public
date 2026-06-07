# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_leap_year (year:int):
    if year%400==0:
        return True
    if year%100==0 and year %400 !=0:
        return False
    elif (year%4==0):
        if not (year %100 ==0):
            return True
    else: 
        return False
     
def list_leap_years (a,b):
    if a>b:
        return "Try again. a must be >= b."
    n=a
    lst_leapyear= []
    while n <= b:
        if is_leap_year(n)==True:
            lst_leapyear.append(n)
        n +=1
    return lst_leapyear
print(list_leap_years(1995, 2005))
# [1996, 2000, 2004]

print(list_leap_years(1896, 1905))
# [1896, 1904]

print(list_leap_years(2019, 2021))
# [2020]

print(list_leap_years(2013, 2015))
# []
