# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(lst):
    if len(lst) < 3:
        return True
    else:
        count = 0
        index = 0
        for n in lst:
            if (index > 0 and index < len(lst) - 1):
                if (n > lst[index - 1] and n > lst[index + 1]) or (n < lst[index - 1] and n < lst[index + 1]):
                    count += 1
            index += 1
        if count == len(lst) - 2:
            return True
        else:
            return False
        
print(is_zigzag([1, 3, 2, 4, 3]))    # True 
print(is_zigzag([1, 4, 2, 5, 3]))    # True 
print(is_zigzag([1, 2, 3, 4]))       # False 
print(is_zigzag([10]))               # True 
print(is_zigzag([1, 3, 2, 4, 5]))    # False