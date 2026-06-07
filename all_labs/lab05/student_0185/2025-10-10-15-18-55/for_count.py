# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(l: list, n: int):
    count = 0
    for i in l:
        if len(i) >= n:
            count += 1
    return count