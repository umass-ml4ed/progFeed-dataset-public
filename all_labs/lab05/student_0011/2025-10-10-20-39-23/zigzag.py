#Author: REDACTED
#Email: REDACTED
#Spire ID: REDACTED

def is_zigzag(integers):
    for i in integers:
        if len(integers)<3:
            return True
        if len(integers)>=3:
            for i in range(1, len(integers)-2):
                if ((integers[i+1]<integers[i] and integers[i-1]<integers[i]) or (integers[i-1]>integers[i] and integers[i+1]>integers[i])):
                    continue
                else:
                    return False
            return True
            
    
print(is_zigzag([1, 3, 2, 4, 3]))    # True 
print(is_zigzag([1, 4, 2, 5, 3]))    # True 
print(is_zigzag([1, 2, 3, 4]))       # False 
print(is_zigzag([10]))               # True 
print(is_zigzag([1, 3, 2, 4, 5]))    # False
  

    