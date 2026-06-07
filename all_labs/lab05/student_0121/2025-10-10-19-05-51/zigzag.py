# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_zigzag(lst): #checks if the list follows a zig zag pattern 
    if len(lst) < 3: 
        return True 
    else: 
        for i in range (1, len(lst)-1): 
            a = lst[i] < lst[i-1] and lst[i] < lst[i+1] 
            b = lst[i] > lst[i-1] and lst[i] > lst[i+1]
            if not (a or b): 
                return False
        return True

print(is_zigzag([1, 3, 2, 4, 3]))    # True 
print(is_zigzag([1, 4, 2, 5, 3]))    # True 
print(is_zigzag([1, 2, 3, 4]))       # False 
print(is_zigzag([10]))               # True 
print(is_zigzag([1, 3, 2, 4, 5]))    # False

        