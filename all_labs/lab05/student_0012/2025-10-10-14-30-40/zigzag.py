# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(lst):

    if len(lst) <= 2:
        return True

    for i in range(1, len(lst) - 1 ):
        if not (i > lst[i+1] and i > lst[i-1]) or (i < lst[i+1] and i < lst[i-1]):
            return False
        return True
        
print(is_zigzag([1, 4, 2, 5, 3]))