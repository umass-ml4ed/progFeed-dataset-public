# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
import math
def is_prime(n):
    i=2
    if n<3:
        return True 
    
    while i<=int(math.sqrt(n)):
        
        if n%i==0:
            return False 
        elif i==int(math.sqrt(n)) and n%i!=0:
            return True
        elif n%i!=0:
            i+=1

        
print(is_prime(2))
        
        
       
