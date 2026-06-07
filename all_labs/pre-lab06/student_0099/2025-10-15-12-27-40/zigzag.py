# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def longest_zigzag_from_start(lst):
    if len(lst) < 2:
        return len(lst)
    
    prev_diff = lst[1] - lst[0]
    if prev_diff == 0:
        return 1
    
    prev_sign = 1 if prev_diff > 0 else -1
    length = 2  
    
    for i in range(2, len(lst)):
        diff = lst[i] - lst[i - 1]
        if diff == 0:
            break
        curr_sign = 1 if diff > 0 else -1
        if curr_sign == prev_sign:
            break
        prev_sign = curr_sign
        length += 1
    
    return length


def zigzag_lengths_from_all_starts(lst):
    result = []
    for i in range(len(lst)):
        result.append(longest_zigzag_from_start(lst[i:]))
    return result

