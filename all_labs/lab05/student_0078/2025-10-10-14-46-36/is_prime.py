# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i <= (n**.5):
        if n % i == 0:
            return False
        i += 1
    return True