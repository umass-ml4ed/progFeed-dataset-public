# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_leap_year(year):
    if(year%400==0):
        return True
    elif(year%100==0):
        return False
    elif(year%4==0):
        return True
    else:
        return False
    
print(is_leap_year(2000))   # True (divisible by 400)
print(is_leap_year(1900))   # False (divisible by 100 but not 400)
print(is_leap_year(2012))   # True (divisible by 4 but not 100)
print(is_leap_year(2019))   # False (not divisible by 4)    

def list_leap_years(a, b):
    leap_lst=[]
    while(a<=b):
        if(is_leap_year(a)):
            leap_lst.append(a)
        a+=1

    return leap_lst

print(list_leap_years(1995, 2005))
# [1996, 2000, 2004]

print(list_leap_years(1896, 1905))
# [1896, 1904]

print(list_leap_years(2019, 2021))
# [2020]

print(list_leap_years(2013, 2015))
# []

