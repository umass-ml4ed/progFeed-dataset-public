# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(n_lst):
    if len(n_lst) < 3:
        return True
    for i in range(1, len(n_lst) - 1):
        middle = n_lst[i]
        left = n_lst[i - 1]
        right = n_lst[i + 1]
        if not ((middle > left and middle > right) or (middle < left and middle < right)):
            return False
        
    return True

print(is_zigzag([1, 3, 2, 4, 3]))    # True 
print(is_zigzag([1, 4, 2, 5, 3]))    # True 
print(is_zigzag([1, 2, 3, 4]))       # False 
print(is_zigzag([10]))               # True 
print(is_zigzag([1, 3, 2, 4, 5]))    # False