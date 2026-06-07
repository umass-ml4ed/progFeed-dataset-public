# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def most_frequent_element(lst):
    if not lst:
        return None  # Handle empty list case
    
    counts = {}  # Dictionary to store frequency of each element
    
    # Count occurrences
    for item in lst:
        counts[item] = counts.get(item, 0) + 1
    
    # Find the key with the highest count
    most_frequent = max(counts, key=counts.get)
    return most_frequent

