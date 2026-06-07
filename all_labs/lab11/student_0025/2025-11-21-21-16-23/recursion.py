# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]
    
    first = lst[0]
    rest = max_recursive(lst[1:])
    
    if first > rest:
        return first
    else:
        return rest


def sum_lists_recursive(lst1, lst2):
    if len(lst1) == 0:
        return 0
    if len(lst1) == 1:
        return lst1[0] + lst2[0]

    first = lst1[0] + lst2[0]
    rest = sum_lists_recursive(lst1[1:], lst2[1:])
    
    return first + rest


def funky(n):
    if n == 0 or n == 1:
        return 1
    elif n % 2 == 0:
        return 2 * funky(n//2)
    else:
        return 1 + 2 * funky(n+1)

