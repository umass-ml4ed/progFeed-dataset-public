# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

# Below, please implement the combine_lists() function as specified in the
# pre-lab instructions.

def combine_lists(a, b):
    """
    Takes two lists of integers, a and b.
    - Insert the first element of b at the beginning of a.
    - Insert the last element of b at the end of a.
    - Delete the middle element of a (assume length is odd before deletion).
    - Return the resulting list a.
    """
    # Insert first element of b at start of a
    a.insert(0, b[0])
    # Insert last element of b at end of a
    a.append(b[len(b) - 1])
    # Delete the middle element of a
    mid_index = len(a) // 2
    del a[mid_index]
    return a


def classify_by_length(a):
    """
    Returns one of: 'empty', 'odd_length', or 'even_length',
    based on the length of list a.
    """
    n = len(a)
    if n == 0:
        return "empty"
    elif n % 2 == 1:
        return "odd_length"
    else:
        return "even_length"


# You can use the code below to help test your functions
# Uncomment the lines to run quick checks.

# print(combine_lists([1, 2, 3], [4, 5, 6, 7]))        # -> [4, 1, 3, 7]
# print(combine_lists([1, 2, 3, 4, 5], [4, 5, 6, 7]))  # -> [4, 1, 2, 4, 5, 7]

# print(classify_by_length([1, 2, 3]))     # -> odd_length
# print(classify_by_length([1, 2, 2, 3]))  # -> even_length
# print(classify_by_length([]))            # -> empty
