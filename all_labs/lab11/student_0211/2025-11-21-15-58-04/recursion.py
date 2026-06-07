# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    partial_max = max_recursive(lst[1:])
    if lst[0] > partial_max:
        return lst[0]
    else: 
        return partial_max
    
def sum_lists_recursive(lst1,lst2):
    if len(lst1) == 0 and len(lst2) == 0:
        return 0
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:],lst2[1:])

def funky(n):
    if n == 0 or n == 1:
        return 1
    elif n%2 == 0 :
        return 2* funky(n//2)
    else:
        return 1 + 2 * funky(n+1)
    
# print(funky(2))
# print(funky(10))
# print(funky(50))
# print(sum_lists_recursive([1, 2, 3], [4, 5, 6])) # returns 21
# print(sum_lists_recursive([2, 3], [5, 6]))       # returns 16
# sum_lists_recursive([3], [6])             # returns 9
# sum_lists_recursive([],[])       
