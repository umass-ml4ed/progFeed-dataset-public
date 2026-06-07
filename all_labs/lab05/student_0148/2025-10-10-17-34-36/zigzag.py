 # Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(lst):
     
    if len(lst) < 3:
        return True
    for i in range(len(lst) - 2):
        if lst[i] == lst[i+1]:
            return False
        if lst[i] > lst[i+1] and lst[i+1] > lst[i+2]:
            return False
        elif lst[i] < lst[i+1] and lst[i+1] < lst[i+2]:
            return False
    return True

print(is_zigzag([1, 3, 2, 4, 3]))    # True 
print(is_zigzag([1, 4, 2, 5, 3]))    # True 
print(is_zigzag([1, 2, 3, 4]))       # False 
print(is_zigzag([10]))               # True 
print(is_zigzag([1, 3, 2, 4, 5]))    # False
