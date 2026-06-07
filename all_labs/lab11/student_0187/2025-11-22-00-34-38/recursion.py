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
    if len(lst1) == 0 and len(lst2) == 0:
        return 0
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])

def funky(n):
    if abs(n) <= 2:
        return n
    if n > 2:
        return funky(n - 2) + 2 * n
    return funky(n + 2) + abs(n)

def permutations(lis):
    if len(lis) == 1:
        return [lis]
    all_perms = []
    for i in range(len(lis)):
        front_item = lis[i]
        remaining = lis[:i] + lis[i+1:]
        smaller_perms = permutations(remaining)
        for p in smaller_perms:
            all_perms.append([front_item] + p)
    return all_perms
