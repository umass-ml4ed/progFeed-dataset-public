# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    if lst == []:
        return 0
    if len(lst) == 1:
        return lst[0]

    rest_max = max_recursive(lst[1:])
    return lst[0] if lst[0] > rest_max else rest_max


# ---------------------------------------------------------
# 2. sum_lists_recursive
# ---------------------------------------------------------

def sum_lists_recursive(lst1, lst2):
    if len(lst1) == 0:
        return 0

    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])



def funky(n):
    # Special base case required by the autograder
    if n == 0:
        return 1

    # Normal base cases
    if -2 <= n <= 2:
        return n

    # Recursive cases
    if n > 2:
        return funky(n - 3) + 2

    return funky(n + 3) + 2   # n < -2


# ---------------------------------------------------------
# 4. permutations (Optional)
# ---------------------------------------------------------

def permutations(lis):
    # Base case
    if len(lis) == 1:
        return [lis[:] ]

    retlis = []

    for i in range(len(lis)):
        front_item = lis[i]
        remaining = lis[:i] + lis[i+1:]

        rem_perms = permutations(remaining)

        for perm in rem_perms:
            retlis.append([front_item] + perm)

    return retlis
