def is_leap_year(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


def list_leap_years(a, b):
    years = []
    current = a
    while current <= b:
        if is_leap_year(current):
            years.append(current)
        current += 1
    return years


print("Testing is_leap_year...")
print(is_leap_year(2000))   # True
print(is_leap_year(1900))   # False
print(is_leap_year(2012))   # True
print(is_leap_year(2019))   # False

print("\\nTesting list_leap_years...")
print(list_leap_years(1995, 2005))   # [1996, 2000, 2004]
print(list_leap_years(1896, 1905))   # [1896, 1904]
print(list_leap_years(2019, 2021))   # [2020]
print(list_leap_years(2011, 2013))   # [])