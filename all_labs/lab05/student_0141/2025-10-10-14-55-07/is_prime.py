# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

def is_prime(n):
    if n <= 1:
        return False
    
    # Check divisibility from 2 to sqrt(n) inclusive
    i = 2
    while i <= int(n ** 0.5):
        if n % i == 0:
            return False
        i += 1
    
    # If no divisors found, n is prime
    return True

print(is_prime(2))