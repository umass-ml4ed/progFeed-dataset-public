# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

def is_prime(n):
    i = 2
    x = n ** 1/2
    while i < x:
        if x % i == 0:
            return False
        i += 1
    return x > 1
