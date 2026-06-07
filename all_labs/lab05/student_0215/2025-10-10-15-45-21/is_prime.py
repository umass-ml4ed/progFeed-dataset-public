# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_prime(n) -> int:
    if n <= 1:
        return False
    divisor = 2
    while divisor <= n ** 0.5:
        if n % divisor == 0:
            return False
        divisor += 1
    return True  

