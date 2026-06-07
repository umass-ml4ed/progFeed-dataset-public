# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def max_recursive(lst):
    if len(lst) == 0:
        return 0
    elif len(lst) == 1:
        return lst[0]
    
    maximum = max_recursive(lst[1:]) 

    if lst[0] > maximum:
        return lst[0]
    else:
        return maximum 

def sum_lists_recursive(lst1,lst2):
    if len(lst1) == 0 and len(lst2) == 0  :
        return 0
    elif len(lst1) == 1 and len(lst2) == 1:
        return lst1[0] + lst2[0]
    
    summation = lst1[0] + lst2[0]
    return summation + sum_lists_recursive(lst1[1:],lst2[1:])

def funky(n):
    if n == 0 or n == 1:
        return 1 
    
    f = funky(n//2)
    f1 = funky(n+1)

    if n % 2 == 0:
        return 2 * f
    else:
        return 1 + f1