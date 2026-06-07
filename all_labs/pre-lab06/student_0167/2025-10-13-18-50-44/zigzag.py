# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def longest_zigzag_from_start(lst):
    if len(lst) < 2:
        return len(lst)
    
    if len(lst) == 2:
        return 2
    
    count = 2
    
    going_up = lst[1] > lst[0]
    
    for i in range(2, len(lst)):
        if going_up:
            if lst[i] < lst[i-1]:
                count += 1
                going_up = False 
            else:
                break  
        else:
            if lst[i] > lst[i-1]:
                count += 1
                going_up = True  
            else:
                break 
    
    return count

print(longest_zigzag_from_start([1, 3, 2, 4, 3]))  # 5 → entire list is zigzag
print(longest_zigzag_from_start([1, 2, 3, 4, 5]))  # 2 → only [1,2] is zigzag
print(longest_zigzag_from_start([3, 1, 4, 2, 5, 6]))  # 5 → [3,1,4,2,5]
print(longest_zigzag_from_start([10]))  # 1 → single element
print(longest_zigzag_from_start([1, 3, 2, 1, 2, 3, 4]))  # 5 → [1,3,2,1,2]

def zigzag_lengths_from_all_starts(lst):
    result = []
    
    # For each starting position in the list
    for start_index in range(len(lst)):
        # Get the zigzag length starting from this position
        zigzag_length = longest_zigzag_from_start(lst[start_index:])
        result.append(zigzag_length)
    
    return result
