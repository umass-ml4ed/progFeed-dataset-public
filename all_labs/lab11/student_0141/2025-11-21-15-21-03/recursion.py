# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    # Base cases
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]
    
    # Recursive case
    return max(lst[0], max_recursive(lst[1:]))

def sum_lists_recursive(lst1, lst2):
    # Base case
    if len(lst1) == 0:
        return 0
    
    # Recursive case
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])

def funky(n):
    # Base case
    if n == 0:
        return 0
    
    # Recursive cases
    if n > 0:
        return n + funky(n - 2)
    else:  # n < 0
        return -n + funky(n + 2)
