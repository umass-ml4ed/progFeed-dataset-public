# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_zigzag(integer_lst):
    if len(integer_lst) < 3:
        return True
    for i in range(1, len(integer_lst) - 1):
        a = integer_lst[i]
        b = integer_lst[i - 1]
        c = integer_lst[i + 1]
        if ((b > a) and (c > a)) or ((b < a) and (c < a)):
            return True     
    return False
print(is_zigzag([1, 3, 2, 4, 3]))    # True 
print(is_zigzag([1, 4, 2, 5, 3]))    # True 
print(is_zigzag([1, 2, 3, 4]))       # False 
print(is_zigzag([10]))               # True 
print(is_zigzag([1, 3, 2, 4, 5]))    # False
