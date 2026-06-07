# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(a, b):
    c = 0
    for i in range(len(a)):
        if len(a[i]) >= int(b):
            c += 1
    return c


