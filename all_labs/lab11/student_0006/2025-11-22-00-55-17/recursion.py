# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]
    maxx = max_recursive(lst[1:])
    if lst[0] > maxx:
        return lst[0]
    else:
        return maxx


def sum_list_recursive(lst1, lst2):
    if len(lst1) == 0:
        return 0
    
    return lst1[0] + lst2[0] + sum_list_recursive(lst1[1:], lst2[1:])

def funky(n):
    if n == 1 or n == 0:
        return 1
    if n % 2 == 0:
        return 2*funky(n//2)
    else:
        return 1 + 2*funky(n+1)
    

    

