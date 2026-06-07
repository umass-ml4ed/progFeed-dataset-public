# Author: REDACTED
# Email: REDACTED
# SPIRE ID: REDACTED


# Description:
#   This program defines a function count_strings(strings, n)
#   that counts how many strings in a given list have at least
#   n characters. It uses a for loop and returns the count.

def count_strings(strings, n):
    """
    Count how many strings in the list have length >= n.

    Parameters:
        strings (list): A list of string elements
        n (int): The minimum number of characters to check for

    Returns:
        int: Number of strings with at least n characters
    """

    count = 0  # Initialize counter variable

    # Loop through each string in the list
    for s in strings:
        # Check if the string length is >= n
        if len(s) >= n:
            count += 1  # Add 1 to count if condition is met

    # After checking all strings, return the total count
    return count


'''# ---------------- Example Test Cases ----------------
# (These are just for testing — the function itself does not print.)

print(count_strings(['', 'a', 'aa', 'aaa'], 0))  # Expected output: 4
print(count_strings(['', 'a', 'aa', 'aaa'], 2))  # Expected output: 2
print(count_strings(['', 'a', 'aa', 'aaa'], 4))  # Expected output: 0

# Edge Case Tests
print(count_strings([], 2))                      # Expected output: 0 (empty list)
print(count_str_'''
