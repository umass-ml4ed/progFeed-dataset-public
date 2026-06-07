# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def max_recursive(lst):
    if  len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]
    return max(lst[0], max_recursive(lst[1:]))
   

def sum_lists_recursive(lst1, lst2):
    if len(lst1) == 0:
        return 0
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])


