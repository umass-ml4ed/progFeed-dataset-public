# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    count = 2
    if len(lst) < 3:
        count = len(lst)
        return count
    for x in range(1, len(lst) - 1):
        if not ((lst[x] > lst[x-1] and lst[x] > lst[x+1]) or (lst[x] < lst[x-1] and lst[x] < lst[x+1])):
            break
        else:
            count += 1
    return count

def zigzag_lengths_from_all_starts(lst):
    ints = []
    for i in range(0,len(lst)):
        ints.append(longest_zigzag_from_start(lst[i:]))
    return ints

print(zigzag_lengths_from_all_starts([1, 3, 2, 4, 3]))  # [5, 4, 3, 2, 1]

print(zigzag_lengths_from_all_starts([1, 2, 3, 4, 5]))  # [2, 2, 2, 2, 1]

print(zigzag_lengths_from_all_starts([3, 1, 4, 2, 5, 6]))  # [5, 4, 3, 2, 2, 1]

print(zigzag_lengths_from_all_starts([10]))  # [1]







