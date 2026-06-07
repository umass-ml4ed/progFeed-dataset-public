# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    comparelst = max_recursive(lst[1:])
    return lst[0] if lst[0] > comparelst else comparelst

    