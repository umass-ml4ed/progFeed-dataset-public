def is_leap_year(yr):
    if yr % 400==0:
        return True
    if yr % 100==0 and yr % 400!=0:
        return False
    if yr%4==0 and yr%100!=0:
        return True
    return False
    
def list_leap_years(a,b):
    leap_years = []
    while a<=b:
        if is_leap_year(a):
            leap_years.append(a)
        a+=1
    return leap_years