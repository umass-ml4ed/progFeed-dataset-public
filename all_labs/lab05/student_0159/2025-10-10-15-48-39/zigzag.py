# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(n):
    if len(n) <= 2:
        return True
    for i in range(0, len(n)-1):
        if not ((n[i] > n[i-1]) & (n[i] > n[i+1])) and not ((n[i] < n[i-1]) & (n[i] < n[i+1])):
            return False
    return True

print(is_zigzag([1, 3, 2, 4, 3]))    # True 
print(is_zigzag([1, 4, 2, 5, 3]))    # True 
print(is_zigzag([1, 2, 3, 4]))       # False 
print(is_zigzag([10]))               # True 
print(is_zigzag([1, 3, 2, 4, 5]))    # False
