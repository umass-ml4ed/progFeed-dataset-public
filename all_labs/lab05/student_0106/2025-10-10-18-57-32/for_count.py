# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(list, n):
    count = 0
    for item in list:
        if len(item) >= n:
            count = count +1
    return count