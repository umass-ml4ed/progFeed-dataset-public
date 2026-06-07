# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(lst, n):
    count = 0
    for index in lst:
        if len(index) >= n:
            count += 1
    return count
