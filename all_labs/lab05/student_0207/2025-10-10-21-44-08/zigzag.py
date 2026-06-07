# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def is_zigzag(list):
    if len(list)<3:
        return True
    for i in range (1,len(list)-1):
        current_i =list[i] 
        left_side=list[i-1]
        right_side=list[i+1]
    
    if not (( current_i > left_side and current_i > right_side) or (current_i< left_side and current_i < right_side)):
        return False 
    
    return True 

print(is_zigzag([1, 3, 2, 4, 3]))    # True 
print(is_zigzag([1, 4, 2, 5, 3]))    # True 
print(is_zigzag([1, 2, 3, 4]))       # False 
print(is_zigzag([10]))               # True 
print(is_zigzag([1, 3, 2, 4, 5]))    # False

