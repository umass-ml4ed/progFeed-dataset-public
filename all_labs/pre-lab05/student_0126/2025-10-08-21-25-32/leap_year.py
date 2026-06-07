# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_leap_year(a):
    return (int(a) % 4 == 0) and ((int(a) % 100 != 0) or int(a) % 400 == 0)

def list_leap_years(a, b):
    d = []
    if int(a) <= int(b):
        while a <= b:
            if is_leap_year(a):
                d.append(a)
            a += 1
    return d

