# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_strings(x,n):
    i = 0
    count = 0
    for s in x:
        if len(x[i]) >= n:
            count += 1
        else:
            i += 1
    return count
