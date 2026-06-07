# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if not lst:
        return 0
    if len(lst) == 1:
        return lst[0]
    max_of_rest = max_recursive(lst[1:])
    if lst[0] > max_of_rest:
        return lst[0]
    else:
        return max_of_rest

def sum_lists_recursive(lst1, lst2):
    if not lst1:
        return 0
    return (lst1[0] + lst2[0]) + sum_lists_recursive(lst1[1:], lst2[1:])

def funky(n):
    if 0 <= n <= 3:
        return n
    elif n > 3:
        return funky(n - 1) + funky(n - 2)
    else:
        return funky(n + 5) - 4

def permutations(lis):
    if len(lis) == 1:
        return [lis]
    retlis = []
    for i in range(len(lis)):
        front_item = lis[i]
        remaining = lis[:i] + lis[i+1:]
        perms_of_remaining = permutations(remaining)
        for p in perms_of_remaining:
            new_permutation = [front_item] + p
            retlis.append(new_permutation)        
    return retlis