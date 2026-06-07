# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_zigzag(a):
    flag =True
    if len(a) < 3: return True 
    for i in range(1, len(a)-1):
        if (a[i + 1] > a[i] > a[i - 1]) or (a[i + 1] < a[i] < a[i - 1]):
            flag= False
    if flag:
        return True
    else:
        return False    
#print(is_zigzag([1, 3, 2, 4, 3]))    # True 
#print(is_zigzag([1, 4, 2, 5, 3]))    # True 
#print(is_zigzag([1, 2, 3, 4]))       # False 
#print(is_zigzag([10]))               # True 
#print(is_zigzag([1, 3, 2, 4, 5]))    # False
