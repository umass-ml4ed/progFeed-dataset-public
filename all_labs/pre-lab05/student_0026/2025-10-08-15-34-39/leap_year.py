# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_leap_year(year):
    return (year%400==0) or (year%4==0 and year%100!=0)



def list_leap_years(a,b):
    leapyears=[]
    while a<=b:
        if is_leap_year(a)==True:
            leapyears.append(int(a))
        a=a+1
    return leapyears
