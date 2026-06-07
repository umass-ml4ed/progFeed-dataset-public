# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    n = len(lst)
    if n < 2:
        return n
    prev_diff = lst[1] - lst[0]
    if prev_diff == 0:
        return 1
    length = 2
    for i in range(2, n):
        diff = lst[i] - lst[i - 1]
        if diff == 0:
            break
        if prev_diff * diff < 0:
            length += 1
            prev_diff = diff
        else:
            break
    return length

def zigzag_lengths_from_all_starts(lst):
    n = len(lst)
    result = []
    for i in range(n):
        result.append(longest_zigzag_from_start(lst[i:]))
    return result
