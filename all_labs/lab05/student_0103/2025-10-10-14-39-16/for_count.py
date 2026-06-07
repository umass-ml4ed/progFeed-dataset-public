# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(list, n):
    count = 0
    for i in list:
        if len(i) >= n:
            count = count + 1
    return count