# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def sum_lists_recursive(lst1, lst2):
    if len(lst1) == 0:
        return 0
    first_sum = lst1[0] + lst2[0]
    return first_sum + sum_lists_recursive(lst1[1:], lst2[1:])
