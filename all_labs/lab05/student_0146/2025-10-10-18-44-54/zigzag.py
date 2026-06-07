# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(l):
    if len(l) < 3:
        return True
    for n in range(1, len(l)-1):
        if not ((l[n] > l[n-1] and l[n] > l[n + 1]) or (l[n] < l[n-1] and l[n] < l[n+1])):
            return False
    return True

print(is_zigzag([1, 3, 2, 4, 3]))    # True 
print(is_zigzag([1, 4, 2, 5, 3]))    # True 
print(is_zigzag([1, 2, 3, 4]))       # False 
print(is_zigzag([10]))               # True 
print(is_zigzag([1, 3, 2, 4, 5]))    # False
