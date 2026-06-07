# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    divisor = 2
    while divisor <= n ** 0.5:
        if n % divisor == 0:
            return False
        else:
            divisor = divisor + 1
    return True
        
        
#print(is_prime(15))      
#print(is_prime(17))      
#print(is_prime(25))   
#print(is_prime(26))      
#print(is_prime(97))
