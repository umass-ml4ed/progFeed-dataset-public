# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED


def is_zigzag(n):

    for i in range(1, len(n) - 1):
        a = n[i - 1]   
        b = n[i]       
        c = n[i + 1]   
        high = b > a and b > c
        low = b < a and b < c
        if high == False and low == False:
            return False
    return True

print(is_zigzag([1, 3, 2, 4, 3]))    # True 
print(is_zigzag([1, 4, 2, 5, 3]))    # True 
print(is_zigzag([1, 2, 3, 4]))       # False 
print(is_zigzag([10]))               # True 
print(is_zigzag([1, 3, 2, 4, 5]))    # False


