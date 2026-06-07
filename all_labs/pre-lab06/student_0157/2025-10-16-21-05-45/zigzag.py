# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    if len(lst) < 2:
        return len(lst)
    length = 1
    up = None # direction

    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            break
        sequence_go_up = lst[i] > lst[i - 1]
        if up is None or sequence_go_up != up: # change direction
            length += 1
            up = sequence_go_up # update direction
        else:
            break 
    return length

def zigzag_lengths_from_all_starts(lst):
    length_list = []
    for start_point in range(len(lst)):
        if len(lst) - start_point < 2:
            length_list.append(len(lst) - start_point)
            continue
        
        length = 1
        up = None 
        for i in range(start_point + 1, len(lst)):
            if lst[i] == lst[i - 1]:
                break
            sequence_go_up = lst[i] > lst[i - 1]
            if up is None or sequence_go_up != up: # change direction
                length += 1
                up = sequence_go_up # update direction
            else:
                break
        length_list.append(length)
    return length_list

print(longest_zigzag_from_start([1, 3, 2, 4, 3]))  # 5 → entire list is zigzag

print(longest_zigzag_from_start([1, 2, 3, 4, 5]))  # 2 → only [1,2] is zigzag (up → not down)

print(longest_zigzag_from_start([3, 1, 4, 2, 5, 6]))  # 5 → [3,1,4,2,5] is longest zigzag from start

print(longest_zigzag_from_start([10]))  # 1 → single element

print(longest_zigzag_from_start([1, 3, 2, 1, 2, 3, 4]))  # 3 → [1,3,2] zigzag from start


print(zigzag_lengths_from_all_starts([1, 3, 2, 4, 3]))  # [5, 4, 3, 2, 1]

print(zigzag_lengths_from_all_starts([1, 2, 3, 4, 5]))  # [2, 2, 2, 2, 1]

print(zigzag_lengths_from_all_starts([3, 1, 4, 2, 5, 6]))  # [5, 4, 3, 2, 2, 1]

print(zigzag_lengths_from_all_starts([10]))  # [1]




