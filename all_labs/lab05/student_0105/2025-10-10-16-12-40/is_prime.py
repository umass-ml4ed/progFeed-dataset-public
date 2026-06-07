# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    i = 2
    while i <= int(n**0.5):
        if n % i != 0:
            i += 1
            if n % i != 0 and i == int(n**0.5):
                return True
            continue
        elif n % i == 0:
            return False
        
print(is_prime(15))            
print(is_prime(17))      
print(is_prime(25))      
print(is_prime(26))      
print(is_prime(97))      





