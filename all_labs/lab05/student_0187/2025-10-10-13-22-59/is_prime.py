# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    if n < 2: return False
    d = 2
    while d <= int(n ** 0.5):
        if n % d == 0:
            return False
        d += 1
    return True

#print(is_prime(15))      
#print(is_prime(17))   
#print(is_prime(25))     
#print(is_prime(26))      
#print(is_prime(97))     

