# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def max_recursive(lst):
    length = len(lst)
    if length == 0:
        return 0
    else:
        return max(lst[0], max_recursive(lst[1:]))

def sum_lists_recursive(lst1, lst2):
    if len(lst1) == 0 or len(lst2) == 0:
        return 0
    else:
        return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])

def funky(n):
    if n == 0 or n == 1:
        return 1
    if n % 2 == 0:
        return 2 * funky(n // 2)
    else:
        return 1 + 2 * funky(n + 1)

def permutations(lst):
    if len(lst) == 1:
        return [lst]
    retlis = []
    for i in range(len(lst)):
        front_item = lst[i]
        remaining = lst[:i] + lst[i+1:]
        for p in permutations(remaining):
            retlis.append([front_item] + p)
    return retlis



