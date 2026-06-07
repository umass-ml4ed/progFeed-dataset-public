# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(lst, n):
    d = 0
    for item in lst:
        if len(item) >= n:
            d += 1
    return d 