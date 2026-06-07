# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def max_recursive(lst):
    if len(lst) == 0:
        return 0
    elif len(lst) == 1:
        return lst[0]
    else:
        first = lst[0]
        max_rest = max_recursive(lst[1:])
        return max_rest

max_recursive([3, 10, 2, 8, 6])