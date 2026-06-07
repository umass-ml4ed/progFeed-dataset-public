

def count_strings(lst:list, n:int):
    
    
    z = len(lst)
    count = 0
    
    for k in range(0, z):
        if len(lst[k]) >= n:
            count += 1
            
    return count

