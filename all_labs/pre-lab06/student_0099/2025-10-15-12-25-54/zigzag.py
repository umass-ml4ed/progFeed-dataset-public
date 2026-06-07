# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def longest_zigzag_from_start(lst):
    if len(lst) < 2:
        return len(lst)
    
    prev_diff = lst[1] - lst[0]
    if prev_diff == 0:
        return 1
    
    prev_sign = 1 if prev_diff > 0 else -1
    length = 2  # the first two form the start of a zigzag
    
    for i in range(2, len(lst)):
        diff = lst[i] - lst[i - 1]
        if diff == 0:
            break
        curr_sign = 1 if diff > 0 else -1
        if curr_sign == prev_sign:
            break
        prev_sign = curr_sign
        length += 1
    
    return length


def zigzag_lengths_from_all_starts(lst):
    result = []
    for i in range(len(lst)):
        result.append(longest_zigzag_from_start(lst[i:]))
    return result


# --- Example tests ---
print(longest_zigzag_from_start([1, 3, 2, 4, 3]))        # 5
print(longest_zigzag_from_start([1, 2, 3, 4, 5]))        # 2
print(longest_zigzag_from_start([3, 1, 4, 2, 5, 6]))     # 5
print(longest_zigzag_from_start([10]))                   # 1
print(longest_zigzag_from_start([1, 3, 2, 1, 2, 3, 4]))  # 3

print(zigzag_lengths_from_all_starts([1, 3, 2, 4, 3]))        # [5, 4, 3, 2, 1]
print(zigzag_lengths_from_all_starts([1, 2, 3, 4, 5]))        # [2, 2, 2, 2, 1]
print(zigzag_lengths_from_all_starts([3, 1, 4, 2, 5, 6]))     # [5, 4, 3, 2, 2, 1]
print(zigzag_lengths_from_all_starts([10]))                   # [1]

