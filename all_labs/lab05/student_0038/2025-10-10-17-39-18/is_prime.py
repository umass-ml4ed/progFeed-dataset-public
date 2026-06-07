# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_prime(n: int):
    divisor = 2
    while divisor >= 2 and divisor <= (n**0.5):
        if n % divisor == 0:
            return False
        divisor += 1
    return True  

