# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(lst, n):
    count = 0
    for s in lst:
        if len(s) >= n:
            count += 1
    return count
