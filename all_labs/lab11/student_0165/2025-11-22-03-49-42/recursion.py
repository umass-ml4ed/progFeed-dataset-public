# Author : REDACTED
# Email: REDACTED
# Spire ID: REDACTED

# returns the maximum element of a list of integers using recursion only.
def max_recursive(lst):
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]
    
    rest_max = max_recursive(lst[1:])
    if lst[0] > rest_max:
        return lst[0]
    else:
        return rest_max

#takes two lists of integers of equal length and returns the summation of the elements of the two input lists
def sum_lists_recursive(lst1, lst2):
    if len(lst1) == 0:
        return 0
    
    first_sum = lst1[0] + lst2[0]
    return first_sum + sum_lists_recursive(lst1[1:], lst2[1:])

#implements the function
def funky(n):
    if n == 0 or n == 1:
        return 1
    
    if n % 2 == 0:    
        return 2 * funky(n // 2)
    
    return 1 + 2 * funky(n + 1)
