# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED



# Q1. 
def max_recursive(list):
    if not list:
        return 0
    
    return max(list[0], max_recursive(list[1:]))


# Q2.
def sum_lists_recursive(lst1, lst2):
    if not lst1:
        return 0
    
    if len(lst1) == 1:
        return lst1[0] + lst2[0]
    
    return (lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:]))


# Q3.
def funky(n):
    if n == 0 or n == 1:
        return 1
    
    if n % 2 == 0:
        return 2 * funky(n//2)
    
    return 1 + 2 * funky(n + 1)