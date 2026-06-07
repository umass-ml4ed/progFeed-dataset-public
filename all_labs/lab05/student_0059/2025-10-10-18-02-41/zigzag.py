# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_zigzag(lis):
    if len(lis) < 3:
        return True
    for i in range(1, len(lis) -1):
        if not (lis[i] >= lis[i-1] and lis[i] >= lis[i+1] or lis[i] <= lis[i-1] and lis[i] <= lis[i+1]):
            return False
    return True
        
print(is_zigzag([1, 3, 2, 4, 3]))    
print(is_zigzag([1, 4, 2, 5, 3]))     
print(is_zigzag([1, 2, 3, 4]))
print(is_zigzag([10]))
print(is_zigzag([1, 3, 2, 4, 5]))
