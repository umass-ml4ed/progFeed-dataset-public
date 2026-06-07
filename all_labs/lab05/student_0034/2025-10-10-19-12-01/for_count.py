# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def count_strings(l: list,n: int)-> int:
    count = 0
    for st in l:
        if len(st) >= n:
            count += 1
    return count
