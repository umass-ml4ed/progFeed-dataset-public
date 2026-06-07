# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    maxi = max_recursive(lst[1:])
    return lst[0] if lst[0] > maxi else maxi

def sum_lists_recursive(lst1, lst2):
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:] + lst2[1:])