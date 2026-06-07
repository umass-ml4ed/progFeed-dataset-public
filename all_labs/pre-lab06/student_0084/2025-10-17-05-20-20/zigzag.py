# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

# Implement the longest_zigzag_from_start function
def longest_zigzag_from_start(lst):
    if len(lst) < 2:
        return len(lst)
    
    length = 1
    initial_difference = lst[1] - lst[0]

    if initial_difference == 0:
        return length
    
    length = 2
    new_difference = initial_difference > 0

    for i in range(2, len(lst)):
        current_difference = lst[i] - lst[i - 1]
        if current_difference == 0:
            break
        
        pos_difference = current_difference > 0
        if pos_difference != new_difference:
            length += 1
            new_difference = pos_difference
        else: 
            break
    return length

print(longest_zigzag_from_start([1, 3, 2, 4, 3]))  # 5 → entire list is zigzag

print(longest_zigzag_from_start([1, 2, 3, 4, 5]))  # 2 → only [1,2] is zigzag (up → not down)

print(longest_zigzag_from_start([3, 1, 4, 2, 5, 6]))  # 5 → [3,1,4,2,5] is longest zigzag from start

print(longest_zigzag_from_start([10]))  # 1 → single element

print(longest_zigzag_from_start([1, 3, 2, 1, 2, 3, 4]))  # 3 → [1,3,2] zigzag from start

# Implement zigzag_lengths_from_all_starts
def zigzag_lengths_from_all_starts(lst):
    lengths = []
    for i in range(len(lst)):
        sublist = lst[i:]  # take the sublist starting from index i
        lengths.append(longest_zigzag_from_start(sublist))
    return lengths

print(zigzag_lengths_from_all_starts([1, 3, 2, 4, 3]))  # [5, 4, 3, 2, 1]

print(zigzag_lengths_from_all_starts([1, 2, 3, 4, 5]))  # [2, 2, 2, 2, 1]

print(zigzag_lengths_from_all_starts([3, 1, 4, 2, 5, 6]))  # [5, 4, 3, 2, 2, 1]

print(zigzag_lengths_from_all_starts([10]))  # [1]
