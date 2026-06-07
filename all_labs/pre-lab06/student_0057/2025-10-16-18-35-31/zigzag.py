# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    n = len(lst)
    if n < 2:
        return n
    prev_diff = lst[1] - lst[0]
    if prev_diff == 0:
        return 1
    length = 2
    for i in range(2, n):
        diff = lst[i] - lst[i - 1]
        if diff == 0:
            break
        if prev_diff * diff < 0:
            length += 1
            prev_diff = diff
        else:
            break
    return length
print(longest_zigzag_from_start([1, 3, 2, 4, 3]))  # 5 → entire list is zigzag
print(longest_zigzag_from_start([1, 2, 3, 4, 5]))  # 2 → only [1,2] is zigzag (up → not down)
print(longest_zigzag_from_start([3, 1, 4, 2, 5, 6]))  # 5 → [3,1,4,2,5] is longest zigzag from start
print(longest_zigzag_from_start([10]))  # 1 → single element
print(longest_zigzag_from_start([1, 3, 2, 1, 2, 3, 4]))  # 3 → [1,3,2] zigzag from start

def zigzag_lengths_from_all_starts(lst):
    n = len(lst)
    result = []
    for i in range(n):
        result.append(longest_zigzag_from_start(lst[i:]))
    return result
print(zigzag_lengths_from_all_starts([1, 3, 2, 4, 3]))  # [5, 4, 3, 2, 1]
print(zigzag_lengths_from_all_starts([1, 2, 3, 4, 5]))  # [2, 2, 2, 2, 1]
print(zigzag_lengths_from_all_starts([3, 1, 4, 2, 5, 6]))  # [5, 4, 3, 2, 2, 1]
print(zigzag_lengths_from_all_starts([10]))  # [1]
