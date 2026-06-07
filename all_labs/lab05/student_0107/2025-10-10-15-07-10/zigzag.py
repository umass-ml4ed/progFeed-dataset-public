# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_zigzag(lst):
    statement = True
    for i in range(len(lst)-1):
        if len(lst) < 3:
            return statement 
        if lst[i] > lst[i-1] and lst[i] > lst[i+1] or lst[i] < lst[i-1] and lst[i] > lst[i+1]:
            statement = True 
        else: 
            statement = False
    return statement 


print(is_zigzag([1, 3, 2, 4, 3]))    # True 
print(is_zigzag([1, 4, 2, 5, 3]))    # True 
print(is_zigzag([1, 2, 3, 4]))       # False 
print(is_zigzag([10]))               # True 
print(is_zigzag([1, 3, 2, 4, 5]))    # False


#list = [1,2,3]
#print(list[-1])