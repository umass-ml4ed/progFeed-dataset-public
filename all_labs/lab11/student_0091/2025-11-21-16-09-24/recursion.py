# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst) == 0:
        return 0

    if len(lst) == 1:
        return lst[0]

    first = lst[0]
    max_rest = max_recursive(lst[1:])

    if first > max_rest:
        return first
    else:
        return max_rest
