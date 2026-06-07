# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

# ---------------------------------------------------------
# 1. max_recursive
# ---------------------------------------------------------

def max_recursive(lst):
    # Base cases
    if lst == []:
        return 0
    if len(lst) == 1:
        return lst[0]

    # Recursive case: compare first element to max of rest
    max_rest = max_recursive(lst[1:])
    return lst[0] if lst[0] > max_rest else max_rest


# ---------------------------------------------------------
# 2. sum_lists_recursive
# ---------------------------------------------------------

def sum_lists_recursive(lst1, lst2):
    # Base case: both empty
    if len(lst1) == 0:
        return 0

    # Recursive step: add fronts + recurse on rest
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])


# ---------------------------------------------------------
# 3. funky (according to the definition given in lecture)
# ---------------------------------------------------------
"""
The function was defined (in lecture) as:

    funky(n) = n                if -2 <= n <= 2
    funky(n) = funky(n-3) + 2   if n > 2
    funky(n) = funky(n+3) + 2   if n < -2

Examples:
funky(2)   = 2
funky(10)  = 74
funky(50)  = 554
funky(-10) = 50
funky(-50) = 418
"""

def funky(n):
    # Base case range
    if -2 <= n <= 2:
        return n

    # Recursive step for large positive n
    if n > 2:
        return funky(n - 3) + 2

    # Recursive step for large negative n
    if n < -2:
        return funky(n + 3) + 2


# ---------------------------------------------------------
# 4. permutations (Optional)
# ---------------------------------------------------------

def permutations(lis):
    # Base case: only 1 permutation
    if len(lis) == 1:
        return [lis[:]]  # return list of lists

    retlis = []

    for i in range(len(lis)):
        front_item = lis[i]

        # remaining list (everything except index i)
        remaining = lis[:i] + lis[i+1:]

        # get permutations of the remaining items
        rem_perms = permutations(remaining)

        # insert front_item at front of each
        for perm in rem_perms:
            retlis.append([front_item] + perm)

    return retlis
