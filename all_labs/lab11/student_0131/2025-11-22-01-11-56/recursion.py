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
    rest_max = max_recursive(lst[1:])
    return lst[0] if lst[0] > rest_max else rest_max


def sum_lists_recursive(lst1, lst2):
    if not lst1:
        return 0
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])


def funky(n):
    # Base cases
    if n == 0:
        return 1
    if -2 <= n <= 2:
        return n
    
    # Positive recursion rule
    if n > 2:
        return funky(n - 3) + 2 * n

    # Negative recursion rule (mirrors the positive case)
    if n < -2:
        return funky(n + 3) - 2 * n
