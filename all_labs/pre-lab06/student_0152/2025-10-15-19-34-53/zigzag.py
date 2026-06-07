# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    if len(lst) < 2:
        return len(lst)
    length = 1
    x = 0
    for i in range (1, len(lst)):
        difference = lst[i] - lst[i-1]
        if difference > 0 and x != 1:
            x = 1
            length += 1
        elif difference < 0 and x != -1:
            x = -1
            length += 1
    return length

print(longest_zigzag_from_start([1, 3, 2, 4, 3]))
print(longest_zigzag_from_start([1, 2, 3, 4, 5]))
print(longest_zigzag_from_start([3, 1, 4, 2, 5, 6]))
print(longest_zigzag_from_start([10]))
print(longest_zigzag_from_start([1, 3, 2, 1, 2, 3, 4]))

def zigzag_lengths_from_all_starts(lst):
    x = []
    for i in range(len(lst)):
        if i == len(lst) - 1:
            x.append(1)
            continue
        length = 1
        difference1 = lst[i + 1] - lst[i]
        if difference1 == 0:
            x.append(1)
            continue
        length = 2
        for j in range(i + 2, len(lst)):
            difference2 = lst[j] - lst[j - 1]
            if (difference1 > 0 and difference2 < 0) or (difference1 < 0 and difference2 > 0):
                length += 1
                difference1 = difference2
            else:
                break
        x.append(length)
    return x

print(zigzag_lengths_from_all_starts([1, 3, 2, 4, 3]))
print(zigzag_lengths_from_all_starts([1, 2, 3, 4, 5]))
print(zigzag_lengths_from_all_starts([3, 1, 4, 2, 5, 6]))
print(zigzag_lengths_from_all_starts([10]))