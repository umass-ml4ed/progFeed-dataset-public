# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(l: list)-> bool:
    if len(l) <= 2:
        return True
    nl = l[1:-1]
    it = 1
    for n in nl:
        if (n > l[it-1] and n > l[it+1]) or (n < l[it-1] and n < l[it+1]):
            it += 1
        else: return False
    return True

print(is_zigzag([1, 3, 2, 4, 3]))    # True 
print(is_zigzag([1, 4, 2, 5, 3]))    # True 
print(is_zigzag([1, 2, 3, 4]))       # False 
print(is_zigzag([10]))               # True 
print(is_zigzag([1, 3, 2, 4, 5]))    # False

