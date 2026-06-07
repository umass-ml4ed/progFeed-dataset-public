# Author    : REDACTED
# Email     : REDACTED
# Spire ID  : REDACTED

def max_recursive(lst):
    if len(lst) == 1: 
        return lst[0]
    first = lst[0]
    max_element = max_recursive(lst[1:])
    return first if first >= max_element else max_element

max_recursive([3, 10, 2, 8, 6]) # returns 10
max_recursive([10, 2, 8, 6])    # returns 10
max_recursive([2, 8, 6])        # returns 8
max_recursive([8, 6])           # returns 8
max_recursive([6])              # returns 6 -> base case
max_recursive([])               # returns 0 -> base case
