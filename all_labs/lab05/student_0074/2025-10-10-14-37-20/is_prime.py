# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_prime(x):
    if x <= 1:
        return False
    i = 2
    while i <= x ** 0.5:
        if x % i == 0:
            return False
        i += 1
    return True

#print(is_prime(15))     
#print(is_prime(17))      
#print(is_prime(25))      
#print(is_prime(26))      
#print(is_prime(97)) 


