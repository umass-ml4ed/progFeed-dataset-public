# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def max_recursive(lst):
    if not lst:
        return 0
    if len(lst) == 1:
        return lst[0]
    return max(max_recursive(lst[:-1]), lst[-1])

def sum_lists_recursive(lst1,lst2):
    if not lst1 and not lst2:
        return 0
    return lst1[-1] + lst2[-1] + sum_lists_recursive(lst1[:-1], lst2[:-1])

def funky(n):
    return (
        1 if n==0 or n==1
        else 2*funky(n//2) if n%2 == 0
        else 1+2*funky(n+1)
    )

def permutations(lis):
    if len(lis) == 1:
        return [lis[:]]
    retlis = []
    last = lis[-1]
    rest = lis[:-1]
    smaller_perms = permutations(rest)
    for perm in smaller_perms:
        for i in range(len(perm) + 1):
            retlis.append(perm[:i]+[last]+perm[i:])
    return retlis