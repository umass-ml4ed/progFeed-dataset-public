# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_strings(lis, n):
    count = 0
    for i in lis:
        if len(i) >= n:
            count += 1
    return count