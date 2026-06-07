# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def count_strings(l: list, n: int):
    number = 0
    for i in l:
        if len(i) >= n:
            number += 1
    return number