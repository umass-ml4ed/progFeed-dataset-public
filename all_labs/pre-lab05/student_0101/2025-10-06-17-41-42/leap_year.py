# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_leap_year(year):
    year=int(year)
    if (year%400==0) :
        return True
    elif ((year%4==0) and (year%100!=0)):
        return True
    elif (year%100==0) and (year%400!=0):
        return False
    else:
        return False 
def list_leap_years(a,b):
    a=int(a)
    b=int(b)
    years=[]
    while a <= b:
        if is_leap_year(a)==True:
            years.append(a)
        a+=1
    return years
print(list_leap_years(1995, 2005))
