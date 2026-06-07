# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def most_frequent_element(lst):
    """
    Returns the element that appears most frequently in the list.
    If multiple elements have the same highest frequency, returns any one of them.
    Returns None if the list is empty.
    """
    if not lst:
        return None  # Handle empty list case
    
    counts = {}  # Dictionary to store frequency of each element
    
    # Count occurrences
    for item in lst:
        counts[item] = counts.get(item, 0) + 1
    
    # Find the key with the highest count
    most_frequent = max(counts, key=counts.get)
    return most_frequent

