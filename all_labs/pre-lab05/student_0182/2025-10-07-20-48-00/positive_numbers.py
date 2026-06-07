# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def filter_positive(numbers):
    """Return a list containing only the positive integers from the input list. Must use a for loop."""
    positives = []
    for num in numbers:
        if num > 0:
            positives.append(num)
    return positives


if __name__ == "__main__":
    print(filter_positive([1, -3, 5, 0, -2, 7]))
    print(filter_positive([-5, -1, -10]))
    print(filter_positive([10, 20, -30, 40]))
