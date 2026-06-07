def is_leap_year(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def list_leap_years(a,b):
    result = []
    for year in range(a, b + 1):
        if is_leap_year(year):
            result.append(year)
    return result

def leap_years_in_range(a, b):
    result = []
    year = a
    while year <= b:
        if is_leap_year(year):
            result.append(year)
        year += 1
    return result
