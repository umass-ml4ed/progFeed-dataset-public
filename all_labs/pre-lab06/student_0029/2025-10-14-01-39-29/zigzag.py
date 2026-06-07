# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    if len(lst) < 2:
        return len(lst)

    count = 1
    prev_diff = 0

    for i in range(1, len(lst)):
        diff = lst[i] - lst[i - 1]
        if diff == 0:
            break
        if prev_diff == 0:
            count +=1
            prev_diff = diff
        else:
            if diff * prev_diff < 0:
                count += 1
                prev_diff = diff
            else:
                break

    return count

def zigzag_lengths_from_all_starts(lst):
    return [longest_zigzag_from_start(lst[i:]) for i in range(len(lst))]

