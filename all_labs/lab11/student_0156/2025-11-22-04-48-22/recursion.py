# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

from typing import List, Union

Number = Union[int, float]


def max_recursive(lst: List[Number]) -> Number:
    """
    Return the maximum element of a list of positive integers/floats using recursion only.
    Base cases:
      - empty list -> return 0
      - single-element list -> return that element
    No loops used.
    """
    if not lst:  # empty list base case
        return 0
    if len(lst) == 1:  # single element base case
        return lst[0]

    # Compare first element with max of rest (recursive call)
    first = lst[0]
    max_rest = max_recursive(lst[1:])
    return first if first >= max_rest else max_rest


def sum_lists_recursive(lst1: List[Number], lst2: List[Number]) -> Number:
    """
    Return the sum of elements from two lists of equal length, computed recursively.
    Assumes lst1 and lst2 have the same length.
    Base case:
      - both empty -> return 0
      - both have length 1 -> return lst1[0] + lst2[0]
    Uses only recursion; no loops.
    """
    if not lst1 and not lst2:
        return 0
    # Add the first elements and recurse on the rest
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])


def funky(n: int) -> int:
    """
    PLACEHOLDER for 'funky' function.

    The original assignment text said "below is the mathematical definition of a funky function"
    but the definition itself was omitted from the prompt I received. To implement this function
    correctly I need that definition (the base cases and the recursive rule).

    Example of what I need (pseudo):
        funky(n) = {
            some base cases (e.g., funky(0) = 0, funky(1) = 1, ...)
            recursive rule for n > 0: funky(n) = funky(n-1) + 2*funky(n-2)  # <-- example only
            recursive rule for n < 0: funky(n) = funky(n+something) + ...
        }

    Please paste the exact mathematical definition/text for funky from your lecture/homework and
    I will update this function with a correct recursive implementation.

    For now this function raises a NotImplementedError so you don't accidentally assume it's implemented.
    """
    raise NotImplementedError(
        "funky is not implemented because the mathematical definition was not provided. "
        "Please provide the recursive formula and I'll implement it."
    )


def permutations(lis: List[object]) -> List[List[object]]:
    """
    Return a list of all permutations of lis (which is a list of unique items).
    Implemented recursively:
      - base case: len(lis) == 1 -> return [lis]
      - otherwise, for each index i, take front_item = lis[i], remaining = lis[:i] + lis[i+1:],
        get perms of remaining recursively, then insert front_item in front of each returned perm.
    """
    if len(lis) == 1:
        return [lis[:]]  # return a list containing a copy of lis

    retlis: List[List[object]] = []

    # We use recursion only; slicing is allowed per instructions.
    for i in range(len(lis)):
        front_item = lis[i]
        remaining = lis[:i] + lis[i + 1 :]
        perms_of_remaining = permutations(remaining)  # recursive call
        # insert front_item at beginning of each permutation and append to retlis
        for perm in perms_of_remaining:
            retlis.append([front_item] + perm)

    return retlis