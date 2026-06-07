# Author    : REDACTED
# Email     : REDACTED
# Spire ID  : REDACTED

def is_zigzag(integers):

    if len(integers) < 3: 
        return True


    for i in range(1, len(integers) - 1):
    
        if not ((integers[i] > integers[i-1] and integers[i] > integers[i+1]) or (integers[i] < integers[i-1] and integers[i] < integers[i+1])): 
            return False

    return True
    
print(is_zigzag([1, 3, 2, 4, 3]))    # True 
print(is_zigzag([1, 4, 2, 5, 3]))    # True 
print(is_zigzag([1, 2, 3, 4]))       # False 
print(is_zigzag([10]))               # True 
print(is_zigzag([1, 3, 2, 4, 5]))    # False
