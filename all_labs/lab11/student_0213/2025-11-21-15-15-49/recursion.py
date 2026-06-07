# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst) == 0:
        return 0
    if lst[0] == max(lst):
        return lst[0]
    lst.pop(0)
    return max_recursive(lst)