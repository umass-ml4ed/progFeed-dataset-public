# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(list):
    count=0
    if (len(list)<3):
        return True
    else:
        for num in range(list[1],list[len(list)-1]):
            if ((num>list[count] and num>list[count+2])  or (num<list[count] and num<list[count+2])):
                count+=1
            else:
                return False
    
    return True
print(is_zigzag([1, 3, 2, 4, 3]))    # True 
print(is_zigzag([1, 4, 2, 5, 3]))    # True 
print(is_zigzag([1, 2, 3, 4]))       # False 
print(is_zigzag([10]))               # True 
print(is_zigzag([1, 3, 2, 4, 5]))    # False


