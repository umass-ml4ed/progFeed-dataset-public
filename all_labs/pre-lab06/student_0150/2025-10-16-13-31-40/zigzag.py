# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    if len(lst) < 2:
        return len(lst)
    
    length = 1  
    prev_diff = 0 
    
    for i in range(1, len(lst)):
        diff = lst[i] - lst[i-1]
        if diff == 0:
            break
        if prev_diff == 0:
            prev_diff = diff
            length += 1
        elif diff * prev_diff < 0:
            prev_diff = diff
            length += 1
        else:
            break
    
    return length


def zigzag_lengths_from_all_starts(lst):
    n = len(lst)
    result = []
    
    for start in range(n): 
        if start == n - 1:
            result.append(1)  
            continue
        
        length = 1
        prev_diff = 0
        
        for i in range(start + 1, n):
            diff = lst[i] - lst[i - 1]
            if diff == 0:
                break
            if prev_diff == 0:
                prev_diff = diff
                length += 1
            elif diff * prev_diff < 0:
                prev_diff = diff
                length += 1
            else:
                break
        
        result.append(length)
    
    return result
