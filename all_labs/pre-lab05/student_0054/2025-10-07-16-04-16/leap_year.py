# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif (year % 4 == 0) and (year % 100 != 0): #4년과 400년 주기=True. 그러나 100년주기는 제외
        return True
    else:
        return False
    
def list_leap_years(a, b):
    leap_years = []
    while a <= b:
        if is_leap_year(a):
            leap_years.append(a)
        a += 1
    return leap_years
        

print(list_leap_years(1995, 2005))  # [1996, 2000, 2004]
print(list_leap_years(2013, 2015))  # []
