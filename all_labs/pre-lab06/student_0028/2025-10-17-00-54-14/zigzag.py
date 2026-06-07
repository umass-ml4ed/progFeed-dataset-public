# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    if len(lst) < 2:
        return len(lst)
    length = 1
    prev_diff = 0
    for i in range(1, len(lst)):
        diff = lst[i] - lst[i - 1]
        if diff == 0:
            break
        if prev_diff == 0 or diff * prev_diff < 0:
            length += 1
            prev_diff = diff
        else:
            break
    return length

def zigzag_lengths_from_all_starts(lst):
    result = []
    for i in range(len(lst)):
        result.append(longest_zigzag_from_start(lst[i:]))
    return result
