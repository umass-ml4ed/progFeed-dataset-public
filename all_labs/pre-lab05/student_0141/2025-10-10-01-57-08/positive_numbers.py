# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def filter_positive(numbers):
    """
    Returns a new list containing only positive integers from the input list.
    """
    result = []
    for num in numbers:
        if num > 0:
            result.append(num)
    return result

