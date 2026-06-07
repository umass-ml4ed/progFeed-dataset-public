# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(list, n):
    n = int(n)
    count = 0
    for i in list:
        if len(i) >= n:
            count += 1
    return count

