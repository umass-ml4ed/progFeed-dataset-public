# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    i = 2
    while i < (int(n ** 0.5)+1): # Start from i and we are going up to the square square number, we are checking all the numbers up to the square root.
        if n % i == 0:
            return False
        i += 1
    return True
print(is_prime(15))      
print(is_prime(17))      
print(is_prime(25))      
print(is_prime(26))      
print(is_prime(97))

    


