# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst) == 0:
        return 0
    elif len(lst) == 1:
        return lst[0]
    else:
        max_of_rest = max_recursive(lst[1:])
        return lst[0] if lst[0] > max_of_rest else max_of_rest

def sum_lists_recursive(lst1, lst2):
    if len(lst1) == 0 and len(lst2) == 0:
        return 0
    else:
        return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])


