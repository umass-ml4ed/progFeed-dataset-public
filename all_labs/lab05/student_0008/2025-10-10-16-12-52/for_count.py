# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(lst, n):
    a = 0
    for i in lst:
        if len(i) >= n:
            a += 1
    return a