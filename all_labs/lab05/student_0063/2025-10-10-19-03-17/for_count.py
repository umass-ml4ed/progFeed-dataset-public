# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_strings(lis, n):
    x = 0
    for char in lis:
        if len(char) >= n:
            x += 1
    return x



