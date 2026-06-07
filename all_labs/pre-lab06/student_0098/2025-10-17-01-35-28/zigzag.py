# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    """
    Returns the length of the longest zigzag subsequence that starts from the first element of the given list.
    
    Args:
        lst (list): A list of integers.
    
    Returns:
        int: The length of the longest zigzag subsequence starting from the first element.
    """
    if len(lst) < 2:
        return len(lst)
    
    zigzag_length = 1
    prev_diff = 0
    
    for i in range(1, len(lst)):
        curr_diff = lst[i] - lst[i-1]
        
        if curr_diff * prev_diff < 0 or prev_diff == 0:
            zigzag_length += 1
            prev_diff = curr_diff
        else:
            break
    
    return zigzag_length

def zigzag_lengths_from_all_starts(lst):
    """
    Returns a list of integers, where each element at index i is the length of the longest contiguous zigzag starting at position i.
    
    Args:
        lst (list): A list of integers.
    
    Returns:
        list: A list of integers, where each element represents the length of the longest zigzag starting at that index.
    """
    result = []
    
    for i in range(len(lst)):
        result.append(longest_zigzag_from_start(lst[i:]))
    
    return result
