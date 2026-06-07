# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def max_recursive(lst):
    if lst == []:
        return 0
    if max(lst) == lst[0]:
        return lst[0]
    return max_recursive(lst[1:])

print(max_recursive([3, 2, 8, 6]))


def sum_lists_recursive(lst1, lst2):
    if lst1 == [] and lst2 == []:
        return sum(lst1[:]) 
    

def funky(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2 * funky(n//2)
    else:
        return 1 + 2 * funky(n+1)
    
#print(funky(2))