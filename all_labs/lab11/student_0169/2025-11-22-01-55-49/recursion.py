# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]
    return max(lst[0], max_recursive(lst[1:]))

def sum_lists_recursive(lst1, lst2):
    if len(lst1) == 0 and len(lst2) == 0:
        return 0
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])

def funky(n):
    if -2 <= n <= 2:
        return n
    if n > 2:
        return funky(n - 5) + funky(n - 2)
    else:  
        return funky(n + 5) + funky(n + 2)

def permutations(lis):
    if len(lis) == 1:
        return [lis]
    retlis = []
    for i in range(len(lis)):
        front_item = lis[i]
        remaining = lis[:i] + lis[i+1:]
        sub_perms = permutations(remaining)
        for perm in sub_perms:
            retlis.append([front_item] + perm)
    return retlis

