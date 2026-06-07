# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    # Base cases
    if lst == []:
        return 0
    if len(lst) == 1:
        return lst[0]

    # Recursive case: compare first element to the max of the rest
    max_rest = max_recursive(lst[1:])
    return lst[0] if lst[0] > max_rest else max_rest

--------------------

def sum_lists_recursive(lst1,
