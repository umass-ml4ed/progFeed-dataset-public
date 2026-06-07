# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def is_leap_year(year):
    while year%400==0:
        return True
    while year%100==0 and year%400!=0:
        return False
    while year%4==0 and year%100!=0:
        return True
    else:
        return False
print(is_leap_year(2000))   # True (divisible by 400)
print(is_leap_year(1900))   # False (divisible by 100 but not 400)
print(is_leap_year(2012))   # True (divisible by 4 but not 100)
print(is_leap_year(2019))  # False (not divisible by 4)

def list_leap_years(a,b):
    years=[]
    while a<=b:
        if is_leap_year(a)==True:
            years.append(a)
            a+=1
        else:
            a+=1
    return years

print(list_leap_years(1995, 2005))
# [1996, 2000, 2004]

print(list_leap_years(1896, 1905))
# [1896, 1904]

print(list_leap_years(2019, 2021))
# [2020]

print(list_leap_years(2013, 2015))
# []


