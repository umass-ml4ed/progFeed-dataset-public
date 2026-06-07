# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    if n < 2:
        return False
    
    # Check for divisibility from 2 to sqrt(n)
    max_divisor = int(n**0.5)
    divisor = 2
    
    while divisor <= max_divisor:
        # Check if n is divisible by current divisor
        if n % divisor == 0:
            return False
        divisor += 1
    
    # If no divisors found, the number is prime
    return True

print(is_prime(15))    
print(is_prime(17))  
print(is_prime(25))
print(is_prime(26))    
print(is_prime(97))  
