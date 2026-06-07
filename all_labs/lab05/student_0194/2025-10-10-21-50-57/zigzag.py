# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(lst):
    for i in range(1, len(lst) - 1):
        if lst[i] > lst[i + 1] and lst[i] > lst[i - 1]:
            continue
        if lst[i] < lst[i + 1] and lst[i] < lst[i - 1]:
            continue
        return False
    return True