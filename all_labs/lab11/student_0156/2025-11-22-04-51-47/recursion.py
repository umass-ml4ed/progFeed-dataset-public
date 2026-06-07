# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

from typing import List, Union

Number = Union[int, float]


def max_recursive(lst: List[Number]) -> Number:
    """Return the max element of the list using recursion only."""
    if not lst:          # empty list
        return 0
    if len(lst) == 1:    # base case
        return lst[0]
    first = lst[0]
    max_rest = max_recursive(lst[1:])
    return first if first >= max_rest else max_rest


def sum_lists_recursive(lst1: List[Number], lst2: List[Number]) -> Number:
    """Return sum of two equal-length lists using recursion only."""
    if not lst1 and not lst2:  # base case
        return 0
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])


def funky(n: int) -> int:
    """
    Implements the recursive function:
        f(0) = 1
        f(1) = 1
        f(n) = 2 * f(n // 2)        if n is even
        f(n) = 1 + 2 * f(n + 1)     otherwise (odd or negative odd)
    """
    # Base cases
    if n == 0 or n == 1:
        return 1

    # Even number rule
    if n % 2 == 0:
        return 2 * funky(n // 2)

    # Odd number rule (includes negative odd)
    return 1 + 2 * funky(n + 1)


def permutations(lis: List[object]) -> List[List[object]]:
    """Return all permutations of a list recursively."""
    if len(lis) == 1:
        return [lis[:]]

    results = []
    for i in range(len(lis)):
        front_item = lis[i]
        remaining = lis[:i] + lis[i+1:]
        perms = permutations(remaining)
        for p in perms:
            results.append([front_item] + p)
    return results