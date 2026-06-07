# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def longest_zigzag_from_start(lst):
    if len(lst) < 2:
        return len(lst)

    length = 1
    direction = 0

    for i in range(1, len(lst)):
        diff = lst[i] - lst[i - 1]
        if diff == 0:
            break
        if direction == 0:
            direction = diff
            length += 1
        elif (direction > 0 and diff < 0) or (direction < 0 and diff > 0):
            direction = diff
            length += 1
        else:
            break
    return length


def zigzag_lengths_from_all_starts(lst):
    result = []
    for i in range(len(lst)):
        sub = lst[i:]
        length = longest_zigzag_from_start(sub)
        result.append(length)
    return result
