# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_strings(x,n):
    count = 0
    for s in x:
        if len(s) >= n:
            count += 1
    return count
