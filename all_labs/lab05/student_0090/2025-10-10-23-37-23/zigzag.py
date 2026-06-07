# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(lis):
    if len(lis) < 3:
        return True
    
    for i in range(1, len(lis) - 1):
        if lis[i] > lis[i+1] and lis[i] > lis[i-1] or lis[i] < lis[i+1] and lis[i] < lis[i-1]:
            continue
        else:
            return False
    
    return True

print(is_zigzag([1, 3, 2, 4, 3]))    # True 
print(is_zigzag([1, 4, 2, 5, 3]))    # True 
print(is_zigzag([1, 2, 3, 4]))       # False 
print(is_zigzag([10]))               # True 
print(is_zigzag([1, 3, 2, 4, 5]))    # False

