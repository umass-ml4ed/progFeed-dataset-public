# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(lis:list):
    if len(lis)<3:
        return True
    for integer in range(1, (len(lis)-1)):
        if (lis[integer] > lis[integer-1] and lis[integer] > lis[integer+1]) or (lis[integer] < lis[integer +1]  and lis[integer] < lis[integer -1]) :
            continue
        else: 
            return False
    return True
        
print(is_zigzag([1, 3, 2, 4, 3]))    # True 
print(is_zigzag([1, 4, 2, 5, 3]))    # True 
print(is_zigzag([1, 2, 3, 4]))       # False 
print(is_zigzag([10]))               # True 
print(is_zigzag([1, 3, 2, 4, 5]))    # False