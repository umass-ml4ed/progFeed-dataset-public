# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst:list):
    x=lst[0]
    if len(lst) == 1:
        return lst[0]
    if len(lst)<1:
        return False
    sub_max = max_recursive(lst[1:])
    return lst[0] if lst[0] > sub_max else sub_max

def sum_lists_recursive(lst1, lst2):
    if len(lst1) == 1:
        return print(lst1[0] + lst2[0])
    return print ((lst1[0] + lst2[0]) + sum_lists_recursive(lst1[1:], lst2[1:]))

def funky(n:int):
    if n == 0 or n == 1:
        return 1
    elif n%2==0:
        return print (2*funky(n//2))
    else:
        return print (1+2*funky(n+1))
