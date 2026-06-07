# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_prime(n:int)->bool:
    if n <= 1:
        return False
    
    prime = n**0.5
    i = 2

    while i <= prime:
        if n % i == 0:
            return False
        i+=1
    return True
        
      

print(is_prime(15))     
print(is_prime(17))