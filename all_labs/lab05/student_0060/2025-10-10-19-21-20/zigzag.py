# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(lst):
    if len(lst) < 3:
        return True
    
    for n in range(1,len(lst)-1):
        if ((lst[n]) > lst[n-1] and lst[n] > lst[n+1]) or ((lst[n]) < lst[n-1] and lst[n] < lst[n+1]):
            return True
    return False

print(is_zigzag([1, 3, 2, 4, 3]))

 

