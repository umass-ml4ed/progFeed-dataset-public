# Author: REDACTED
# Email: REDACTED
# SPIRE ID: REDACTED


# Description:
#   This program defines a function is_zigzag(lst) that checks whether
#   a list of integers follows a zigzag pattern or not.
# ---------------------------------------------------------------------

def is_zigzag(lst):
    """
    Determine whether a list follows a zigzag pattern.
    
    Parameters:
        lst (list): A list of integers.
    
    Returns:
        bool: True if the list is zigzag, False otherwise.
    """

    # A list with fewer than 3 elements automatically follows zigzag pattern
    if len(lst) < 3:
        return True

    # Loop through the list, skipping the first and last elements
    for i in range(1, len(lst) - 1):

        # Current element
        middle = lst[i]
        # Neighbors
        left = lst[i - 1]
        right = lst[i + 1]

        # Check if middle is strictly greater than both neighbors (a "peak")
        # OR strictly smaller than both neighbors (a "valley")
        if not ((middle > left and middle > right) or (middle < left and middle < right)):
            # If neither condition is true, it violates the zigzag rule
            return False

    # If loop completes with no violations, it's zigzag
    return True


'''# ---------------- Example Test Cases ----------------
print(is_zigzag([1, 3, 2, 4, 3]))   # Expected: True (up-down-up-down)
print(is_zigzag([1, 4, 2, 5, 3]))   # Expected: True
print(is_zigzag([1, 2, 3, 4]))      # Expected: False (always increasing)
print(is_zigzag([10]))              # Expected: True (only one element)
print(is_zigzag([1, 3, 2, 4, 5]))   # Expected: False (last pair breaks pattern)
'''