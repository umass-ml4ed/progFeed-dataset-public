# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def max_recursive(lst):
    i = 0
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]
    inside = max_recursive(lst[1:])
    return lst[0] if lst[0] > inside else inside

def sum_lists_recursive(lst1, lst2):
    x = len(lst1) 
    if x <= 0:
        return 0
    z = lst1[x] + lst2[x]
    y = x - 1
    return z + sum_lists_recursive(lst1, lst2)

sum_lists_recursive([1, 2, 3], [4, 5, 6])

