# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def max_recursive(lst):
    """
    Return the maximum element of lst using recursion only.
    Base cases:
      - empty list -> return 0 (per problem spec)
      - single-element list -> that element
    Assumes elements are positive ints/floats when present.
    """
    if not lst:
        return 0
    if len(lst) == 1:
        return lst[0]
    # compare first element with max of rest
    rest_max = max_recursive(lst[1:])
    return lst[0] if lst[0] >= rest_max else rest_max


def sum_lists_recursive(lst1, lst2):
    """
    Sum all elements from two lists of equal length using recursion only.
    Base case: both empty -> 0
    """
    if not lst1 and not lst2:
        return 0
    # assume lengths are equal and at least 1 if not both empty
    return lst1[0] + lst2[0] + sum_lists_recursive(lst1[1:], lst2[1:])


def permutations(lis):
    """
    Return all permutations of lis (list of unique items).
    This uses recursion plus a loop to iterate choices for the front item.
    Returns a list of lists.
    """
    if len(lis) == 1:
        return [lis[:]]  # return a list containing a copy of lis
    retlis = []
    for i in range(len(lis)):
        front_item = lis[i]
        remaining = lis[:i] + lis[i+1:]
        for perm in permutations(remaining):
            retlis.append([front_item] + perm)
    return retlis


def funky(n):
    """
    Placeholder for the 'funky' function.

    NOTE: The mathematical definition of 'funky' was not included in the prompt.
    You gave examples:
      funky(2)  = 2
      funky(10) = 74
      funky(50) = 554
      funky(-10)= 50
      funky(-50)= 418

    Those examples are insufficient to uniquely determine a single natural recursive
    definition. Please paste the exact mathematical (recursive) definition you want
    implemented (e.g. a piecewise recurrence like "if n <= 0: f(n) = f(n+11); else: f(n)=f(n-10)"),
    or confirm the intended rule, and I will implement it recursively.

    For now this raises NotImplementedError so you notice the missing definition.
    """
    raise NotImplementedError("funky's mathematical definition was not provided. Please supply it.")


# --- quick self-tests ---
if __name__ == "__main__":
    # max_recursive tests
    assert max_recursive([3, 10, 2, 8, 6]) == 10
    assert max_recursive([6]) == 6
    assert max_recursive([]) == 0

    # sum_lists_recursive tests
    assert sum_lists_recursive([1,2,3], [4,5,6]) == 21
    assert sum_lists_recursive([], []) == 0
    assert sum_lists_recursive([3], [6]) == 9

    # permutations tests
    assert permutations(['AA']) == [['AA']]
    two = permutations(['AA','BB'])
    assert sorted(two) == sorted([['AA','BB'], ['BB','AA']])

    print("Implemented functions pass the quick checks. Provide funky's definition and I'll implement it.")
