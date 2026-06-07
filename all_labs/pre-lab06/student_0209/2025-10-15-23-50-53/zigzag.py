
# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def longest_zigzag_from_start(lst):
    if len(lst) < 2:
        return len(lst)
    length = 1
    direction = 0
    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            if direction != 1:
                length += 1
                direction = 1
            else:
                break
        elif lst[i] < lst[i - 1]:
            if direction != -1:
                length += 1
                direction = -1
            else:
                break
        else:
            break
    return length

def zigzag_lengths_from_all_starts(lst):
    lengths = []
    for i in range(len(lst)):
        lengths.append(longest_zigzag_from_start(lst[i:]))
    return lengths
    


    