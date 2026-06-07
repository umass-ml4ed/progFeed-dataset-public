# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]
    
    max = max_recursive(lst[1:])
    return lst[0] if lst[0] > max else max



print(max_recursive([2]))
