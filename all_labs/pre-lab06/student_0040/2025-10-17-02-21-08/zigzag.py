



def longest_zigzag_from_start(lst):
    if len(lst) < 2:
        return len(lst)
    
    length = 1
    prev_diff = lst[1] - lst[0]
    
    if prev_diff != 0:
        length = 2
    else:
        prev_diff = 0
    
    for i in range(2, len(lst)):
        diff = lst[i] - lst[i - 1]
        
        if diff == 0:
            break
        if prev_diff * diff < 0:  
            length += 1
            prev_diff = diff
        else:
            break
    
    return length