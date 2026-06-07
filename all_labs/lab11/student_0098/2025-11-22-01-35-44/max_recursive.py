
# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def max_recursive(lst):
    if not lst:
        return 0
    
    if len(lst) == 1:
        return lst[0]
    
    max_rest = max_recursive(lst[1:])
    
    if lst[0] > max_rest:
        return lst[0]
    else:
        return max_rest



