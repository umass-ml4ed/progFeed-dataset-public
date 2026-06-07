# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    return max(lst[0], max_recursive(lst[1:]))

def sum_lists_recursive(lst1, lst2):
    if len(lst1) == 0:
        return 0
    if len(lst1) != len(lst2):
        return 0
    summation = lst1[0] + lst2[0]
    return summation + sum_lists_recursive(lst1[1:], lst2[1:])

def funky(n):
    if n == 1 or n == 0:
        total = 1
    elif n%2==0:
        total = 2*(funky(n//2))
    else:
        total = 1+2*(funky(n+1))
    return total
    
