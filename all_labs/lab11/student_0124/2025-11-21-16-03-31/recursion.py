# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def max_recursive(x: list) -> float:

    if len(x) == 0:

        return 0

    if len(x) == 1:

        return x[0]

    return max(x[0], max_recursive(x[1:]))


def sum_lists_recursive(lst1: list, lst2: list) -> list:

    if len(lst1) == 0:

        return 0

    sum = lst1[0] + lst2[0]

    lst1 = lst1[1:]

    lst2 = lst2[1:]

    return sum + sum_lists_recursive(lst1, lst2)


def funky(n: int) -> float:

    if n == 0 or n == 1:

        return 1

    if n % 2 == 0:

        return 2 * funky(n//2)

    return 1 + (2 * funky(n + 1)) 

def permutations(lst: list) -> int:

    l = len(lst)

    if l == 1:

        return 1
    
    lst1 = lst[1:]

    return l * permutations(lst1)

