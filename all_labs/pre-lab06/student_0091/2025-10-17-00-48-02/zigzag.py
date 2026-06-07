# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst)->int:
    n = len(lst)
    if n < 2:
        return n

    length = 1
    prev_diff = None

    for i in range(1, n):
        diff = lst[i] - lst[i - 1]

        if diff == 0:
            break

        elif prev_diff== None:
            length += 1
            prev_diff = diff
        elif diff * prev_diff < 0:
            length += 1
            prev_diff = diff
        else:
            break

    return length


def zigzag_lengths_from_all_starts(lst):
    result = []
    n = len(lst)

    for i in range(n):
        sub_length = longest_zigzag_from_start(lst[i:])
        result.append(sub_length)

    return result


print(zigzag_lengths_from_all_starts([1, 3, 2, 4, 3]))  # [5, 4, 3, 2, 1]

print(zigzag_lengths_from_all_starts([1, 2, 3, 4, 5]))  # [2, 2, 2, 2, 1]

print(zigzag_lengths_from_all_starts([3, 1, 4, 2, 5, 6]))  # [5, 4, 3, 2, 2, 1]

print(zigzag_lengths_from_all_starts([10]))  # [1]

