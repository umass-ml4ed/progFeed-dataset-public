# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def sum_lists_recursive(lst1, lst2):
    if not lst1 and not lst2:

return 0 return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])

