# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i <= int(n ** 0.5):
        if n % i == 0:
            return False
        i += 1
    
    return True

print(is_prime(17))

#print(is_prime(7))       #False
#print(is_prime(17))      #True
#print(is_prime(25))      #False
#print(is_prime(26))      #False
#print(is_prime(97))      #True