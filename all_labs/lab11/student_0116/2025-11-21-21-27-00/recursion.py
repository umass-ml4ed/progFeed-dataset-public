# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if not lst:
        return 0
    if len(lst) == 1:
        return lst[0]
    else:
        max_of_rest = max_recursive(lst[1:])
        return lst[0] if lst[0] > max_of_rest else max_of_rest

def sum_lists_recursive(lst1, lst2):
    if not lst1 and not lst2:
        return 0
    else:
        return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])

def funky(n):
    if n == 0 or n == 1:
        return 1
    elif n > 1:
        return n + funky(n - 2)
    else:
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