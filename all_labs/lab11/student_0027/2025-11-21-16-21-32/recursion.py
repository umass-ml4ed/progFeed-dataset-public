# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]
    m = max_recursive(lst[1:])
    return lst[0] if lst[0] > m else m

def sum_lists_recursive(lst1, lst2):
    if len(lst1) == 0:
        return 0
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])

def funky(n):
    if n == 0:
        return 0
    if n > 0:
        return n + funky(n - 2)
    return -n + funky(n + 2)

def permutations(lis):
    if len(lis) == 1:
        return [lis]
    retlis = []
    for i in range(len(lis)):
        front_item = lis[i]
        remaining = lis[:i] + lis[i+1:]
        for p in permutations(remaining):
            retlis.append([front_item] + p)
    return retlis