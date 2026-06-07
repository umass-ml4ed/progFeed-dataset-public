# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(lst):
    # Lists with fewer than 3 elements are always zigzag
    if len(lst) < 3:
        return True

    # Check each middle element
    for i in range(1, len(lst) - 1):
        if not ((lst[i] > lst[i - 1] and lst[i] > lst[i + 1]) or
                (lst[i] < lst[i - 1] and lst[i] < lst[i + 1])):
            return False
    return True
