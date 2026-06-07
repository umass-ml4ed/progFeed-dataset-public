# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
def is_zigzag(lst):
    # If the list has fewer than 3 elements, it's automatically zigzag
    if len(lst) < 3:
        return True

    # Loop through all elements except the first and last
    for i in range(1, len(lst) - 1):
        # Check if the current element is bigger than both neighbors
        if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
            continue  # It's zigzag at this position, move to next
        # Check if the current element is smaller than both neighbors
        elif lst[i] < lst[i - 1] and lst[i] < lst[i + 1]:
            continue  # It's zigzag at this position, move to next
        else:
            return False  # Not zigzag, exit early

    # If all elements passed the checks, the list is zigzag
    return True
    