


def is_zigzag(lst:list):

    
    if len(lst) < 3:
        return True
    else:
        
        
        for k in range(1, len(lst) - 1):
            
            lower = (lst[k-1] < lst[k]) and (lst[k+1] < lst[k])
            upper = (lst[k-1] > lst[k]) and (lst[k+1] > lst[k]) 
  
            if not (lower or upper):
                return False
            
                
    return True



    
# 5 - 1
# 0 1 2 3 4 5






print(is_zigzag([1, 3, 2, 4, 3]))    # True 
print(is_zigzag([1, 4, 2, 5, 3]))    # True 
print(is_zigzag([1, 2, 3, 4]))       # False 
print(is_zigzag([10]))               # True 
print(is_zigzag([1, 3, 2, 4, 5]))    # False
