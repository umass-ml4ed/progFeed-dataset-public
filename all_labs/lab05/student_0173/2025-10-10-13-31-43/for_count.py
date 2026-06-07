# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_strings(lst, n):
    counter = 0
    for i in lst:
        if len(i) >= n:
            counter += 1
        else:
            continue
    return counter