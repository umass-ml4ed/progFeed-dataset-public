# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_zigzag(list_of_int):
    if len(list_of_int) < 3:
        return True
    for i in range(1, len(list_of_int) - 1):
        left = list_of_int[i - 1]
        middle = list_of_int[i]
        right = list_of_int[i + 1]

        above = middle > left and middle > right
        below = middle < left and middle < right
        if not above and not below:
            return False
    return True

print(is_zigzag([1, 3, 2, 4, 3]))    # True 
print(is_zigzag([1, 4, 2, 5, 3]))    # True 
print(is_zigzag([1, 2, 3, 4]))       # False 
print(is_zigzag([10]))               # True 
print(is_zigzag([1, 3, 2, 4, 5]))    # False
