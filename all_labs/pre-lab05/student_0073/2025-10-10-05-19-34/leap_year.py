# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_leap_year(year) -> int:
    if year % 400 == 0:
        return (True)
    elif year % 100 == 0:
        if year % 400 != 0:
            return (False)
    elif year % 4 == 0:
        if year % 100 != 0:
            return(True)
    else:
        return (False)


