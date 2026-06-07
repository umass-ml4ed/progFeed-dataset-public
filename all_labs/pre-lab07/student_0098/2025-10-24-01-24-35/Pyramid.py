# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def pyramid(n):
    """
    Generates a pyramid-like pattern of numbers.

    Args:
        n (int): A positive integer representing the number of lines in the pattern.

    Returns:
        None
    """
    for i in range(n, 0, -1):
        # Create a string of numbers from i down to 1, separated by a space
        line = ' '.join(str(j) for j in range(i, 0, -1))
        # Print the line and add a newline character
        print(line)
        print()
