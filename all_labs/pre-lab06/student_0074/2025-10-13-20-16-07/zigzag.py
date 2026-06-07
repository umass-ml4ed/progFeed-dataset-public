# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def longest_zigzag_from_start(lst):
    if (len(lst) < 2):
        return len(lst)  
    
    length = 1 
    first_diff = lst[1] - lst[0]
    
    if (first_diff != 0):
        length = 2 

    for i in range(1, len(lst) - 1):
        diff = lst[i + 1] - lst[i]
        if (diff == 0):
            continue
        if (first_diff * diff < 0):
            length += 1
            first_diff = diff
        else:
            break  
    return length

#print(longest_zigzag_from_start([1, 3, 2, 4, 3]))  # 5 → entire list is zigzag
#print(longest_zigzag_from_start([1, 2, 3, 4, 5]))  # 2 → only [1,2] is zigzag (up → not down)
#print(longest_zigzag_from_start([3, 1, 4, 2, 5, 6]))  # 5 → [3,1,4,2,5] is longest zigzag from start
#print(longest_zigzag_from_start([10]))  # 1 → single element
#print(longest_zigzag_from_start([1, 3, 2, 1, 2, 3, 4]))  # 3 → [1,3,2] zigzag from start

def zigzag_lengths_from_all_starts(lst):
    result = []
    for i in range(len(lst)):
        length = 1  
        if (i < len(lst) - 1):
            first_diff = lst[i + 1] - lst[i]
            if (first_diff != 0):
                length = 2  
            for j in range(i + 1, len(lst) - 1):
                diff = lst[j + 1] - lst[j]
                if (diff == 0):
                    break  
                if (first_diff * diff < 0):  
                    length += 1
                    first_diff = diff
                else:
                    break 
        result.append(length)
    return result

#print(zigzag_lengths_from_all_starts([1, 3, 2, 4, 3]))  # [5, 4, 3, 2, 1]
#print(zigzag_lengths_from_all_starts([1, 2, 3, 4, 5]))  # [2, 2, 2, 2, 1]
#print(zigzag_lengths_from_all_starts([3, 1, 4, 2, 5, 6]))  # [5, 4, 3, 2, 2, 1]
#print(zigzag_lengths_from_all_starts([10]))  # [1]

