#Author: REDACTED
#Spire ID: REDACTED
#Email: REDACTED

def max_recursive(lst):
    # Base case: empty list
    if not lst:
        return 0   # assignment specifies returning 0
    # Base case: single element
    if len(lst) == 1:
        return lst[0]
    # Recursive case
    return max(lst[0], max_recursive(lst[1:]))

def sum_lists_recursive(lst1, lst2):
    # Base case: both lists empty
    if not lst1 and not lst2:
        return 0
    # Recursive case: add first elements + recurse on rest
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])

def funky(n):
    # Base cases
    if n == 0:
        return 1
    if n == 1 or n == -1:
        return 1
    # Recursive cases
    if n > 0:
        return n + funky(n - 2)
    else:
        return -n + funky(n + 2)

def permutations(lis):
    # Base case: single item
    if len(lis) == 1:
        return [lis]
    retlis = []
    # Recursive case: choose each item as front, permute the rest
    for i in range(len(lis)):
        front_item = lis[i]
        remaining = lis[:i] + lis[i+1:]
        for perm in permutations(remaining):
            retlis.append([front_item] + perm)
    return retlis
