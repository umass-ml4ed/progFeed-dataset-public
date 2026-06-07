# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(lst):
    if len(lst)<3:
        return True
    for number in range(1, len(lst)-1):
        index=lst[number]
        left=lst[number-1]
        right=lst[number+1]
        if not((index>left and index>right)or (index<left and index<right)):
            return False
    return True

print(is_zigzag([1, 3, 2, 4, 3]))    # True 
print(is_zigzag([1, 4, 2, 5, 3]))    # True 
print(is_zigzag([1, 2, 3, 4]))       # False 
print(is_zigzag([10]))               # True 
print(is_zigzag([1, 3, 2, 4, 5]))    # False

