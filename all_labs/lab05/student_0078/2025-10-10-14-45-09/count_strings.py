# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def for_count(lis, n):
    count = 0
    for i in lis:
        if len(i) >= n:
            count += 1
    return count