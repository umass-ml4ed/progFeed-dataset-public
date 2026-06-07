# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(lis):
    if(len(lis)<3):
        return True
    b = len(lis)
    c = lis[1:-1:2]
    for i in c:
        g = lis.index(i)
        if not (i>lis[g-1] and i>lis[g+1] or i<lis[g-1] and i<lis[g+1]):
            return False
    return True
print(is_zigzag([1, 3, 2, 4, 3]))    # True 
print(is_zigzag([1, 4, 2, 5, 3]))    # True 
print(is_zigzag([1, 2, 3, 4]))       # False 
print(is_zigzag([10]))               # True 
print(is_zigzag([1, 3, 2, 4, 5]))    # False

