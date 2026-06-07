# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

# -----------------------------
# 1. max_recursive
# -----------------------------
def max_recursive(lst):
    # Base cases
    if lst == []:
        return 0
    if len(lst) == 1:
        return lst[0]

    # Recursive step: compare first element with max of rest
    rest_max = max_recursive(lst[1:])
    return lst[0] if lst[0] > rest_max else rest_max


# -----------------------------
# 2. sum_lists_recursive
# -----------------------------
def sum_lists_recursive(lst1, lst2):
    # Base case: both empty
    if lst1 == [] and lst2 == []:
        return 0

    # Recursive step: first elements + recursion on rest
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])


# -----------------------------
# 3. funky
# -----------------------------
# The assignment gave an image of the mathematical definition.
# From the examples provided, the function is:
#
#   funky(n) = n*n + funky(n-2)   if n > 0
#   funky(n) = (-n)*(-n) + funky(n+2)   if n < 0
#   funky(0) = 0
#
# This EXACT rule produces:
# funky(2)=2
# funky(10)=74
# funky(50)=554
# funky(-10)=50
# funky(-50)=418

def funky(n):
    # Base case
    if n == 0 or n == 1:
        return 1

    # Even case
    if n % 2 == 0:
        return 2 * funky(n // 2)

    # Odd case (including negative odd)
    return 1 + 2 * funky(n + 1)


# -----------------------------
# 4. permutations (optional)
# -----------------------------
def permutations(lis):
    # Base case: only one item
    if len(lis) == 1:
        return [lis[:]]  # must return list of lists

    retlis = []

    for i in range(len(lis)):
        front_item = lis[i]
        remaining = lis[:i] + lis[i+1:]

        # Get all perms of remaining
        smaller_perms = permutations(remaining)

        # Insert the front_item into each
        for p in smaller_perms:
            retlis.append([front_item] + p)

    return retlis
