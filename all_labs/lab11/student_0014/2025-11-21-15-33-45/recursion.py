# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    return max_recursive(lst[0]) if max_recursive(lst[0]) > max_recursive(lst[1:]) else max_recursive(lst[1:])


max_recursive([3, 10, 2, 8, 6]) # returns 10
max_recursive([10, 2, 8, 6])    # returns 10
max_recursive([2, 8, 6])        # returns 8
max_recursive([8, 6])           # returns 8
max_recursive([6])              # returns 6 -> base case
max_recursive([])               # returns 0 -> base case


