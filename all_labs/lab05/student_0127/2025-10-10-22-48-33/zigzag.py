# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(lst):
    if len(lst) < 3:
        return True
    for i in range(1, len(lst) - 1):
        prev = lst[i - 1]
        curr = lst[i]
        nxt = lst[i + 1]

        if not ((curr > prev and curr > nxt) or (curr < prev and curr < nxt)):
            return False 
    return True
