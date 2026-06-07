#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

def is_leap_year(year: int) -> bool:
    return ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0))

def list_leap_years(a: int, b: int) -> list:
    years_to_check = list(range(a,(b+1)))
    i = 0
    list_to_return = []
    while i < len(years_to_check):
        if is_leap_year(years_to_check[i]):
            list_to_return.append(years_to_check[i])
        i += 1
    return list_to_return





