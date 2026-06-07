# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    first = lst[0]
    max_of_rest = max_recursive(lst[1:])
    return first if first > max_of_rest else max_of_rest

def sum_lists_recursive(lst1, lst2):
    if not lst1 and not lst2:
        return 0
    first_sum = lst1[0] + lst2[0]
    rest_sum = sum_lists_recursive(lst1[1:], lst2[1:])
    return [first_sum] + [rest_sum]

def funky(n):
    if n == 1 or n == 0:
        return 1
    if n % 2 == 0:
        return 2 * funky(n//2)
    else:
        return 1 + (2 *funky(n + 1))