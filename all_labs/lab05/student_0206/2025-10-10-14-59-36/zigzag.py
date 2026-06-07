# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(l: list):
    if len(l) < 3:
        return True
    for i in range(1, len(l) - 1):
        current = l[i]
        last = l[i - 1]
        next = l[i + 1]
        condition1 = current > last and current > next
        condition2 = current < last and current < next
        if not condition1 and not condition2:
            return False
    return True

print(is_zigzag([1, 3, 2, 4, 3]))    # True 
print(is_zigzag([1, 4, 2, 5, 3]))    # True 
print(is_zigzag([1, 2, 3, 4]))       # False 
print(is_zigzag([10]))               # True 
print(is_zigzag([1, 3, 2, 4, 5]))    # False
