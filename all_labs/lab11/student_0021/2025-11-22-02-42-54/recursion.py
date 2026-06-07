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


def sum_lists_recursive(lst1, lst2):
    if lst1 == []:
        return 0
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])


def funky(n):
    if n == 0:
        return 0
    if n > 0:
        return funky(n - 1) + 2 * n
    else:
        return funky(n + 1) + 2 * n
