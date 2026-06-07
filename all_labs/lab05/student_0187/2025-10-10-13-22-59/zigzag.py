# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_zigzag(num):
    if len(num) < 3: 
        return True
    for i in range(1, len(num)-1):
        if not ((num[i] > num[i-1] and num[i] > num[i+1]) or (num[i] < num[i-1] and num[i] < num[i+1])):
            return False
    return True

#print(is_zigzag([1, 3, 2, 4, 3]))    
#print(is_zigzag([1, 4, 2, 5, 3]))    
#print(is_zigzag([1, 2, 3, 4]))      
#print(is_zigzag([10]))               
#print(is_zigzag([1, 3, 2, 4, 5]))    

