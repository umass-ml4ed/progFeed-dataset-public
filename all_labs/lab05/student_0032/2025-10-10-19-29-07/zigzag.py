# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def is_zigzag(list: list):
    variable = 0
    if len(list) < 3:
        return True
    for whatever in range(1, len(list)-1):
        if (list[whatever] > list[whatever-1] and list[whatever] > list[whatever+1]) or (list[whatever] < list[whatever-1] and list[whatever] < list[whatever+1]):
            variable += 1
    if variable == len(list)-2:
        return True    
    else:
        return False 
        

print(is_zigzag([1, 3, 2, 4, 3]))   
print(is_zigzag([1, 4, 2, 5, 3]))   
print(is_zigzag([1, 2, 3, 4]))       
print(is_zigzag([10]))              
print(is_zigzag([1, 3, 2, 4, 5]))   
