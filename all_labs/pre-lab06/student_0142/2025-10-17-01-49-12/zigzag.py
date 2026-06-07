# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    n = len(lst)
    if n < 2:
        return n  # fewer than 2 elements count as zigzag
    
    length = 1
    prev_diff = 0
    
    for i in range(1, n):
        diff = lst[i] - lst[i-1]
        if diff == 0:
            break
        if prev_diff == 0:
            prev_diff = diff
            length += 1
        else:
            # check if current difference alternates sign from prev_diff
            if (diff > 0 > prev_diff) or (diff < 0 < prev_diff):
                length += 1
                prev_diff = diff
            else:
                break

    return length

print(longest_zigzag_from_start([1, 3, 2, 4, 3]))  # 5
print(longest_zigzag_from_start([1, 2, 3, 4, 5]))  # 2
print(longest_zigzag_from_start([3, 1, 4, 2, 5, 6]))  # 5
print(longest_zigzag_from_start([10]))  # 1
print(longest_zigzag_from_start([1, 3, 2, 1, 2, 3, 4]))  # 3

def zigzag_lengths_from_all_starts(lst):
    n = len(lst)
    if n == 0:
        return []
    if n == 1:
        return [1]

    lengths = [1] * n  # Minimum length for each position is 1

    for i in range(n - 2, -1, -1):  # Start from second last element back to 0
        diff = lst[i+1] - lst[i]
        if diff == 0:
            lengths[i] = 1
            continue
        length = 1
        prev_diff = diff
        length += 1
        for j in range(i + 2, n):
            diff = lst[j] - lst[j - 1]
            if diff == 0 or (diff > 0 and prev_diff > 0) or (diff < 0 and prev_diff < 0):
                break
            length += 1
            prev_diff = diff
        lengths[i] = length

    return lengths

print(zigzag_lengths_from_all_starts([1, 3, 2, 4, 3]))  # [5, 4, 3, 2, 1]
print(zigzag_lengths_from_all_starts([1, 2, 3, 4, 5]))  # [2, 2, 2, 2, 1]
print(zigzag_lengths_from_all_starts([3, 1, 4, 2, 5, 6]))  # [5, 4, 3, 2, 2, 1]
print(zigzag_lengths_from_all_starts([10]))  # [1]

