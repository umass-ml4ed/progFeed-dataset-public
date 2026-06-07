# Author: REDACTED
# Email: REDACTED
# SpireID: REDACTED


def max_recursive(lst):
    # Base cases
    if lst == []:
        return 0
    if len(lst) == 1:
        return lst[0]

    # Recursive step: compare first element with max of rest
    rest_max = max_recursive(lst[1:])
    return lst[0] if lst[0] > rest_max else rest_max

def sum_lists_recursive(lst1, lst2):
    # Base case
    if lst1 == [] and lst2 == []:
        return 0

    # Recursive step: sum heads + recurse on tails
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])

def funky(n):
    # base cases
    if n == 0 or n == 1:
        return 1
    
    # even case
    if n % 2 == 0:
        return 2 * funky(n // 2)
    
    # odd case
    else:
        return 1 + 2 * funky(n + 1)