# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if not lst:
        return 0
    if len(lst) == 1:
        return lst[0]
    supermax = max_recursive(lst[1:]) 
    return lst[0] if lst[0] >  supermax else supermax

def sum_lists_recursive(lst1, lst2):
    if len(lst1) == 0: 
        return 0
    if len(lst2) == 0:
        return 0
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])

def funky(n):
    if n == 0 or n == 1:
        return 1
    if n % 2 == 0:
        return 2 * funky(n//2)
    return 1+2 * funky(n+1)    

print(funky(2))