# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    # Base cases
    if len(lst) == 0:
        return 0
    if len(lst) == 1:
        return lst[0]
    
    # Recursive case
    return max(lst[0], max_recursive(lst[1:]))

def sum_lists_recursive(lst1, lst2):
    # Base case
    if len(lst1) == 0:
        return 0
    
    # Recursive case
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])

def funky(n):
    if n == 0:
        return 1
    if n == 1 or n == -1:
        return 1

    if n > 0:
        return n + funky(n - 2)
    else:  # n < 0
        return -n + funky(n + 2)



def permutations(lis):
    # Base case: if there's only one item, return it as the only permutation
    if len(lis) == 1:
        return [lis]
    
    retlis = []  # This will store all permutations
    
    # Loop through each index (allowed in optional section)
    for i in range(len(lis)):
        front_item = lis[i]                   # Pick current element
        remaining = lis[:i] + lis[i+1:]       # All other elements
        
        # Recursively get permutations of remaining elements
        for perm in permutations(remaining):
            retlis.append([front_item] + perm)
    
    return retlis
