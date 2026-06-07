# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    n = len(lst)
    if n < 2:
        return n

    first_diff = lst[1] - lst[0]
    if first_diff == 0:
        return 1

    length = 2
    prev_diff = first_diff

    for i in range(2, n):
        diff = lst[i] - lst[i - 1]
        if diff == 0:
            break
        if (prev_diff > 0 and diff < 0) or (prev_diff < 0 and diff > 0):
            length += 1
            prev_diff = diff
        else:
            break

    return length

