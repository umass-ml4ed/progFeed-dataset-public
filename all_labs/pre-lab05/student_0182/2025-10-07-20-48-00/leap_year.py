# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_leap_year(year):
    """Return True if year is a leap year, otherwise False."""
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


def list_leap_years(a, b):
    """Return a list of all leap years between a and b (inclusive). Must use a while loop."""
    leap_years = []
    year = a
    while year <= b:
        if is_leap_year(year):
            leap_years.append(year)
        year += 1
    return leap_years


if __name__ == "__main__":
    print(is_leap_year(2000))
    print(is_leap_year(1900))
    print(is_leap_year(2012))
    print(is_leap_year(2019))

    print(list_leap_years(1995, 2005))
    print(list_leap_years(1896, 1905))
    print(list_leap_years(2019, 2021))
    print(list_leap_years(2013, 2015))
