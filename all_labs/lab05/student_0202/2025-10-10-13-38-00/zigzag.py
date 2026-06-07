# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(list):
    if len(list) < 3:
            return True
    i = 1
    while i < len(list) - 1:
        if (list[i-1] > list[i] and list[i] < list[i+1]) or (list[i-1] < list[i] and list[i] > list[i+1]):
            i += 1
        else:
            return False
    return True
        
print(is_zigzag([1, 3, 2, 4, 3]))    # True 
print(is_zigzag([1, 4, 2, 5, 3]))    # True 
print(is_zigzag([1, 2, 3, 4]))       # False 
print(is_zigzag([10]))               # True 
print(is_zigzag([1, 3, 2, 4, 5]))    # False
