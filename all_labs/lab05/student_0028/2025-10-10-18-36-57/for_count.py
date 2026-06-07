# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def count_strings(lst,n):
    c = 0
    for s in lst:
        if len(s) >= n: c += 1
    return c
