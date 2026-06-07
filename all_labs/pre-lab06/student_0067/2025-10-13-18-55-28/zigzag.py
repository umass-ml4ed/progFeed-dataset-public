# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def longest_zigzag_from_start(lst: list) -> int:
    if len(lst) < 2:
        return len(lst)
    prev_diff = lst[1] - lst[0]
    
    zigzag = 2 if prev_diff != 0 else 1
    for i in range(1, len(lst) - 1):
        
        diff = lst[i+1] - lst[i]
        if diff > 0 and prev_diff < 0:
            zigzag += 1
        elif diff < 0 and prev_diff > 0:
            zigzag += 1
        else:
            break
        prev_diff = diff
    return zigzag



def zigzag_lengths_from_all_starts(lst: list) -> list:
    z_lengths = []
    for i in range(len(lst)):
        z_lengths.append(longest_zigzag_from_start(lst[i:]))
    return z_lengths
        
