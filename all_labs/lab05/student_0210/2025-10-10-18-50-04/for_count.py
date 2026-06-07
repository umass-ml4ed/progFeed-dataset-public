# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_strings(List, n):
    count = 0
    for x in List:
        if len(x) >= n:
            count += 1
    return count