# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

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
    
def sum_lists_recursive(lst1, lst2):
    # base case: both empty
    if len(lst1) == 0:
        return 0
    
    # recursive case: first pair + sum of rest
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])

def funky(n):
    # base case
    if n == 0 or n == 1:
        return 1

    # if n is even
    if n % 2 == 0:
        return 2 * funky(n // 2)

    # otherwise (odd numbers and negatives)
    return 1 + 2 * funky(n + 1)



