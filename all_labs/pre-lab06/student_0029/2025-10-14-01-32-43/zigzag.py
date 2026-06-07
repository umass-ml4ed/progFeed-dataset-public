# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    if len(lst) < 2:
        return len(lst)

    count = 1
    direction = 0  # 0: no direction, 1: up, -1: down

    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            if direction != 1:
                count += 1
                direction = 1
        elif lst[i] < lst[i - 1]:
            if direction != -1:
                count += 1
                direction = -1

    return count

def zigzag_lengths_from_all_starts(lst):
    lengths = []
    for i in range(len(lst)):
        lengths.append(longest_zigzag_from_start(lst[i:]))
    return lengths

