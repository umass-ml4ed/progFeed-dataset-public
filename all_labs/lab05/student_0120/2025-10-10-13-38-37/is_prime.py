# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    root_n = int(n**0.5)
    while root_n>=2:
        if n % root_n == 0:
            return False
        else:
            root_n = root_n - 1
    else:
        return True

    
print(is_prime(15))      
print(is_prime(17))      
print(is_prime(25))     
print(is_prime(26))      
print(is_prime(97))    

