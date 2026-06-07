# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(strings, n):
    count = 0
    for s in strings:
        if len(s) >= n:
            count += 1
    return count