# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(lst):
    for i in range(1, len(lst) - 1):
        if not ((lst[i] > lst [i-1] and lst[i] > lst[i+1]) or (lst[i] < lst[i-1] and lst[i] < lst[i+1])):
            return False
    return True