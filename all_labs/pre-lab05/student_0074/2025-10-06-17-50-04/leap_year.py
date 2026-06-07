def is_leap_year(x):
    if(x%400 == 0):
        return True
    elif(x%4 == 0 and not x%100 == 0):
        return True
    else:
        return False

#print(is_leap_year(2000))   
#print(is_leap_year(1900))   
#print(is_leap_year(2012))  
#print(is_leap_year(2019)) 


def list_leap_years(a, b):
    leap_years = []
    while (a <= b):
        if is_leap_year(a):
            leap_years.append(a)
        a = a+1
    return leap_years

#print(list_leap_years(1995, 2005))
#print(list_leap_years(1896, 1905))
#print(list_leap_years(2019, 2021))
#print(list_leap_years(2011, 2013))


