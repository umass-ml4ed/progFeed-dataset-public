# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def is_leap_year(years:int):
    return years%400 == 0 or (years%4==0 and years%100!= 0)

def list_leap_years(a,b):
    leap_list = []
    a = int(a)
    b = int(b)
    while a<=b:
        if is_leap_year(a) == True : 
            leap_list.append(a)
        a+=1
    return(leap_list)

print(list_leap_years(1995, 2005))






    



