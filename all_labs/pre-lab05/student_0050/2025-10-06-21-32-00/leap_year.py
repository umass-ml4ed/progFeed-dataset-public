# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_leap_year(year)->bool:
    if (year%400==0):
        return True
    elif(year%100==0):
        return False
    elif(year%4==0):
        return True
    else:
        return False

def list_leap_years(a,b)->[]:
    lis=[]
    while a<=b:
        if(is_leap_year(a)==True):
            lis.append(a)
        a = a+1
    return lis


print(list_leap_years(1995, 2005))
# [1996, 2000, 2004]

print(list_leap_years(1896, 1905))
# [1896, 1904]

print(list_leap_years(2019, 2021))
# [2020]

print(list_leap_years(2013, 2015))
# []


