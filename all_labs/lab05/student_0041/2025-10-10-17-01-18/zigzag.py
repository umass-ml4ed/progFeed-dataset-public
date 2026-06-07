# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(lst):
    if(len(lst) < 3):
        zigzag = True
    count = 0
    zigzag = True
    for index in range(1, len(lst) - 1):
        front = lst[index - 1]
        end = lst[index + 1]
        if(lst[index] >= front and lst[index] <= end) or (lst[index] <= front and lst[index] >= end):
            zigzag = False
        count += 1
    return zigzag

print(is_zigzag([1, 3, 2, 4, 3]))    # True 
print(is_zigzag([1, 4, 2, 5, 3]))    # True 
print(is_zigzag([1, 2, 3, 4]))       # False 
print(is_zigzag([10]))               # True
print(is_zigzag([1, 3, 2, 4, 5]))    # False