# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

# zigzag.py

def is_zigzag(data: list[int]) -> bool:
    """
    Checks if a list of integers follows a zigzag pattern.

    A list is zigzag if every element (except the first and last) is either:
    - Strictly greater than both its neighbors, or
    - Strictly smaller than both its neighbors.

    A list with fewer than 3 elements is considered a zigzag pattern.

    Args:
        data: A list of integers.

    Returns:
        True if the list follows a zigzag pattern, False otherwise.
    """
    if len(data) < 3:
        return True

    for i in range(1, len(data) - 1):
        current_element = data[i]
        left_neighbor = data[i - 1]
        right_neighbor = data[i + 1]

        
        is_peak = current_element > left_neighbor and current_element > right_neighbor

        
        is_valley = current_element < left_neighbor and current_element < right_neighbor

        
        if not (is_peak or is_valley):
            return False

    return True
