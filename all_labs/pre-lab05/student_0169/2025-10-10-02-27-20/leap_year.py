def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def list_leap_years(a, b):
    leap_years = []
    year = a
    while year <= b:
        if is_leap_year(year):
            leap_years.append(year)
        year += 1
    return leap_years
