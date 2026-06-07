# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    n = len(lst)
    if n < 2:
        return n
    if lst[1] == lst[0]:
        return 1
    length = 2
    old_diff = lst[1] - lst[0]
    for i in range(2, n):
        new_diff = lst[i] - lst[i - 1]
        if new_diff == 0:
            break
        if (old_diff > 0 and new_diff < 0) or (old_diff < 0 and new_diff > 0):
            length += 1
            old_diff = new_diff
        else:
            break
    return length

def zigzag_lengths_from_all_starts(lst):
    lengths = []
    for i in range(len(lst)):
        sub_list = lst[i:]
        lengths.append(longest_zigzag_from_start(sub_list))
    return lengths