# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(lst):
    if len(lst)<3:
        return True
    
    for i in range(1, len(lst)-1):
        a=lst[i]
        b=lst[i-1]
        c=lst[i+1]
        if not ((a>b and a>c) or (a<b and a<c)):
            return False        
    return True

print(is_zigzag([1, 3, 2, 4, 3]))    
print(is_zigzag([1, 4, 2, 5, 3]))    
print(is_zigzag([1, 2, 3, 4]))       
print(is_zigzag([10]))               
print(is_zigzag([1, 3, 2, 4, 5]))    