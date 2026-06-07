# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(strings, x):
    count = 0
    for i in strings:
        if len(i) >= x:
            count += 1
    return count