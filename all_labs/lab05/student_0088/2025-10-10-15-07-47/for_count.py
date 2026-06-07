# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_strings(strings, n):
    count = 0
    for i in strings:
        if len(i) >= n:
            count += 1
    return count