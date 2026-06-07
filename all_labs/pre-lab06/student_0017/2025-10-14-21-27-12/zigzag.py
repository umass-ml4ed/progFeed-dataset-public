# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    if len(lst) < 2:
        return len(lst)

    length = 1  # always count the first element
    prev_diff = lst[1] - lst[0]

    if prev_diff != 0:
        length = 2
    else:
        return 1  # no zigzag if first two are equal

    for i in range(2, len(lst)):
        diff = lst[i] - lst[i - 1]
        if diff == 0:
            break
        # sign must alternate
        if (prev_diff > 0 and diff < 0) or (prev_diff < 0 and diff > 0):
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

print(zigzag_lengths_from_all_starts([1, 3, 2, 4, 3]))
print(zigzag_lengths_from_all_starts([1, 2, 3, 4, 5]))
print(zigzag_lengths_from_all_starts([10]))