# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def max_recursive(lst: list):
    if not lst:
        return 0
    elif len(lst) == 1:
        return lst[0]
    first_elem = lst[0]
    max_num = max_recursive(lst[1:])
    if first_elem > max_num:
        return first_elem
    else:
        return max_num

def sum_lists_recursive(lst1: list, lst2: list):
    if not (lst1 and lst2):
        return 0
    first_sum = lst1[0] + lst2[0]
    next_sum = sum_lists_recursive(lst1[1:], lst2[1:])
    return first_sum + next_sum

def funky(n: int):
    if (n == 0) or (n == 1):
        return 1
    if n % 2 == 0:
        return 2 * funky(n//2)
    else:
        return 1 + 2 * funky(n + 1)
