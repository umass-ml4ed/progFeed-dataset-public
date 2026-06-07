# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    elif len(lst) == 0:
        return 0
    else:
        return max(lst[0], max_recursive(lst[1:len(lst)]))
    

def sum_lists_recursive(lst1, lst2):
    if len(lst1) == 0:
        return 0
    elif len(lst1) == 1:
        return lst1[0] + lst2[0]
    else:
        nl1 = lst1[:]
        nl2 = lst2[:]
        nl1[1] = nl1[0] + nl1[1]
        nl2[1] = nl2[0] + nl2[1]
        nlst1 = nl1[1:]
        nlst2 = nl2[1:]
        return sum_lists_recursive(nlst1, nlst2)

def funky(n):
    if n == 0 or n == 1:
        return 1
    elif n//2 == 0:
        return 2*funky(n//2)
    else:
        return 1+2*funky(n+1)
