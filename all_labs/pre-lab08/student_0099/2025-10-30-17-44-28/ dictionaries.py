# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def most_frequent_element(lst):
    if not lst:
        return None
    
    counts = {}
    for item in lst:
        counts[item] = counts.get(item, 0) + 1
    
    # Find the element with the highest count
    return max(counts, key=counts.get)



