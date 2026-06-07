# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(s, n):
    count = 0
    for characters in s:
        d = len(characters)
        if d >= n:
            count += 1
    return count