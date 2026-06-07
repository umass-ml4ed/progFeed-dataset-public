# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(a):
    if (len(a)<3):
        return True
    for i in range(1,(len(a)-1)):
        main_i = a[i]
        prev_i = a[i-1]
        next_i = a[i+1]
        if ((main_i > prev_i) and (main_i > next_i)):
            continue
        elif ((main_i < prev_i) and (main_i < next_i)):
            continue
        else:
            return False
        
    return True
        

print(is_zigzag([1, 3, 2, 4, 3]))    # True 
print(is_zigzag([1, 4, 2, 5, 3]))    # True 
print(is_zigzag([1, 2, 3, 4]))       # False 
print(is_zigzag([10]))               # True 
print(is_zigzag([1, 3, 2, 4, 5]))    # False







