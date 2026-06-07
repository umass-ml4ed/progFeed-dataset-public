# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst) == 0:
        return 0
    elif len(lst) == 1:
        return lst[0]
    max = max_recursive(lst[1:])
    return lst[0] if lst[0] > max else max

def sum_lists_recursive(lst1, lst2):
    if len(lst1) == 0 and len(lst2) == 0:
        return 0
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])
def funky(n):
    n=int(n)
    if n == 0 or n == 1:
        return 1
    elif n%2 == 0:
        return 2*funky(n//2)
    return 1 + 2*funky(n+1)