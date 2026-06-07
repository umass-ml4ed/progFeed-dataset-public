# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def longest_zigzag_from_start(lst):
    if (len(lst) < 2):
        return len(lst)

    length = 1 
    p_diff = lst[1] - lst[0]

    if (p_diff != 0):
        length = 2

    for i in range(1, len(lst) - 1):
        diff = lst[i + 1] - lst[i]
        if (diff == 0):
            continue  
        if (p_diff * diff < 0):
            length += 1
            p_diff = diff
        else:
            break  
    return length


#print(longest_zigzag_from_start([1, 3, 2, 4, 3]))  # 5 → entire list is zigzag
#print(longest_zigzag_from_start([1, 2, 3, 4, 5]))  # 2 → only [1,2] is zigzag (up → not down)
#print(longest_zigzag_from_start([3, 1, 4, 2, 5, 6]))  # 5 → [3,1,4,2,5] is longest zigzag from start
#print(longest_zigzag_from_start([10]))  # 1 → single element
#print(longest_zigzag_from_start([1, 3, 2, 1, 2, 3, 4]))  # 3 → [1,3,2] zigzag from start

def zigzag_lengths_from_all_starts(lst):
    res = []
    
    for i in range(len(lst)):
        if (i == len(lst) - 1):
            res.append(1)
            continue
        
        length = 1
        p_diff = lst[i + 1] - lst[i]

        if (p_diff != 0):
            length = 2 

        for j in range(i + 1, len(lst) - 1):
            diff = lst[j + 1] - lst[j]
            if (diff == 0):
                break 
            if (p_diff * diff < 0):
                length += 1
                p_diff = diff
            else:
                break  
        res.append(length)
    return res

#print(zigzag_lengths_from_all_starts([1, 3, 2, 4, 3]))  # [5, 4, 3, 2, 1]
#print(zigzag_lengths_from_all_starts([1, 2, 3, 4, 5]))  # [2, 2, 2, 2, 1]
#print(zigzag_lengths_from_all_starts([3, 1, 4, 2, 5, 6]))  # [5, 4, 3, 2, 2, 1]
#print(zigzag_lengths_from_all_starts([10]))  # [1]

