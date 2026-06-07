# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(ints):
    if len(ints) < 3:
        return True
    else:
        for x in range(1, len(ints) - 1):
            if not (ints[x] > ints[x-1] and ints[x] > ints[x+1]) or (ints[x] < ints[x-1] and ints[x] < ints[x+1]):
                return False
            return True

#print(is_zigzag([1, 3, 2, 4, 3]))    # True 
#print(is_zigzag([1, 4, 2, 5, 3]))    # True 
#print(is_zigzag([1, 2, 3, 4]))       # False 
#print(is_zigzag([10]))               # True 
#print(is_zigzag([1, 3, 2, 4, 5]))    # False
