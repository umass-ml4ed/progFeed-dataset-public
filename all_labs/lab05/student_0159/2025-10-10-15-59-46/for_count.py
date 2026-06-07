# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(a,n):
    b = 0
    for i in a:
        if len(i) >= n:
            b += 1
    return b

