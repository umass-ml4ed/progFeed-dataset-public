# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(lis, n):
    count = 0
    for s in lis:
        if len(s) >= n:
            count += 1
    return count