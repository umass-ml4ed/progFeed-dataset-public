# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    if len(lst) < 2:
        return len(lst)
    length = 1
    prev_diff = lst[1] - lst[0]
    if prev_diff == 0:
        return 1
    length = 2
    for i in range(2, len(lst)):
        diff = lst[i] - lst[i - 1]
        if diff == 0:
            break
        if (diff > 0 and prev_diff < 0) or (diff < 0 and prev_diff > 0):
            length += 1
            prev_diff = diff
        else:
            break
    return length


def zigzag_lengths_from_all_starts(lst):
    result = []
    for i in range(len(lst)):
        sub_length = longest_zigzag_from_start(lst[i:])
        result.append(sub_length)
    return result
