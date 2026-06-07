


def is_zigzag(lst:list):
    
    ans = 0
    
    if len(lst) < 3:
        return ans == 0
    else:
        
        
        for k in range(1, len(lst) - 1):
            
            if not (lst[k] > lst[k+1] and lst[k] > lst[k-1]) or (lst[k] < lst[k+1] and lst[k] < lst[k-1]):
                ans += 1
            else:
                print("yes")
            
                
    return ans == 0 


    
# 5 - 1
# 0 1 2 3 4 5






print(is_zigzag([1, 3, 2, 4, 3]))    # True 
print(is_zigzag([1, 4, 2, 5, 3]))    # True 
print(is_zigzag([1, 2, 3, 4]))       # False 
print(is_zigzag([10]))               # True 
print(is_zigzag([1, 3, 2, 4, 5]))    # False
