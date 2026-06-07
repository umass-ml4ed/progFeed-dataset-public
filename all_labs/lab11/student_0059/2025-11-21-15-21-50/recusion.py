# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def max_recursive(lst):
    if len(lst) == 0:
        return
    return lst[0] 


def sum_lists_recursive(lst1, lst2):
    if lst1 == [] and lst2 == []:
        return 0
    

def funky(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2 * funky(n//2)
    else:
        return 1 + 2 * funky(n+1)
    
print(funky(2))