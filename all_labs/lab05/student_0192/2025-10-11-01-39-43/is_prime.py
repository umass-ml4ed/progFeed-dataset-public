# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


def is_prime(n):
    p = 2
    n1=  n**0.5
    if n<2:
        return False
    while p<=n1:
        if n%p == 0:
            return False
        p+=1
    return True
        
        
        
    
            
        
print(is_prime(15))      
print(is_prime(17))      
print(is_prime(25))      
print(is_prime(26))      
print(is_prime(97))      

     




