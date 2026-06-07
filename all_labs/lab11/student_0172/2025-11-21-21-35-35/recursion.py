# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]
    rest_max = max_recursive(lst[1:])
    if lst[0] > rest_max:
        return lst[0]
    else:
        return rest_max
    

def sum_lists_recursive(lst1, lst2):
    if lst1 == []:
        return 0
    
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])
    

def funky(n):
    if n == 0 or n == 1:
        return 1

    if n % 2 == 0:
        return 2 * funky(n // 2)

    return 1 + 2 * funky(n + 1)