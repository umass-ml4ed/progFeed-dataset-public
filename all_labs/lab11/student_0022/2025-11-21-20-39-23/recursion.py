# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst) == 0:
        return 0
    maximum = lst[0]
    length = len(lst)
    if length == 1:
        return lst[-1]
    if maximum < lst[1]:
        new_lst = lst[1:]
        return max_recursive(new_lst)
    elif maximum > lst[1]:
        lst.pop(1)
        return max_recursive(lst)

def sum_lists_recursive(lst1, lst2):
    if len(lst1) == 0:
        return 0
    elif len(lst1) == 1:
        return lst1[0] + lst2[0]
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])

def funky(n):
    if n==0 or n==1:
        return 1
    elif n % 2 == 0:
        return 2 * funky(n//2)
    else:
        return 1 + 2*funky(n+1)
    
