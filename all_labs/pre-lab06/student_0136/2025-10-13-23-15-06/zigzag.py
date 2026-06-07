# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    length = 1
    diff = 0
    pdiff = 0
    for i in range(1, len(lst)):
        diff = lst[i]-lst[i-1]
        if (diff > 0 and pdiff <= 0):
            length = length + 1
            pdiff = diff
        elif (diff < 0 and pdiff >= 0):
            length = length + 1
            pdiff = diff
        else:
            break
    return length

print(longest_zigzag_from_start([1, 3, 2, 4, 3]))  # 5 → entire list is zigzag
print(longest_zigzag_from_start([1, 2, 3, 4, 5]))  # 2 → only [1,2] is zigzag (up → not down)
print(longest_zigzag_from_start([3, 1, 4, 2, 5, 6]))  # 5 → [3,1,4,2,5] is longest zigzag from start
print(longest_zigzag_from_start([10]))  # 1 → single element
print(longest_zigzag_from_start([1, 3, 2, 1, 2, 3, 4]))  # 3 → [1,3,2] zigzag from start

def zigzag_lengths_from_all_starts(lst):
    new_lst = []
    for i in range(len(lst)):
        temp = lst[i:]
        new_lst.append(longest_zigzag_from_start(temp))
    return new_lst

print(zigzag_lengths_from_all_starts([1, 3, 2, 4, 3]))  # [5, 4, 3, 2, 1]
print(zigzag_lengths_from_all_starts([1, 2, 3, 4, 5]))  # [2, 2, 2, 2, 1]
print(zigzag_lengths_from_all_starts([3, 1, 4, 2, 5, 6]))  # [5, 4, 3, 2, 2, 1]
print(zigzag_lengths_from_all_starts([10]))  # [1]
