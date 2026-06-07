# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(l, n):
    c = 0
    for s in l:
        if len(s) >= n:
            c +=1
    return c